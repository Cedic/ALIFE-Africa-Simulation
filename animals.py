# Import
from random import randint
from constants import *
from visual import * 
from textures import *
import Image

# Functions
def dna_to_int(dna):
    return int("".join(str(i) for i in dna), 2)


def random_dna():
    dna = []
    for i in range(4):
        dna.append(randint(0,1))
    return dna


##############################################################################


# Classes
class Animal:
    def __init__(self, dna):
        self.dna = dna

        self.pos = [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        self.nrj_max = 250 + randint(-50,50)
        self.nrj = self.nrj_max/2
        self.life_expect = 1000 + randint(-200,200) # In number of iterations

        dnaint = dna_to_int(self.dna)
        self.speed = dnaint + 1
        self.vision = dnaint*2 + 1
        self.food_eaten = dnaint/2 + 1
        self.nrj_consum = float(dnaint)/4 + 1

        # Graphic model
        self.model = sphere(pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF,5), radius=VCOEFF/2)

    def alive(self):
        return self.nrj > 0

    def reproduct(self, animal2):
        dim = len(self.dna)
        new_dna = []
        fixed_point = randint(0,dim)
        for i in range(dim):
            if i < fixed_point:
                new_dna.append(self.dna[i])
            else:
                new_dna.append(animal2.dna[i])
        return new_dna
        
    def move_model(self, x, y):
        for i in range(VCOEFF):
            self.model.pos=(self.pos[0]+x, self.pos[1]+y, 5)
            range(SIM_SPEED)

    def live(self):
        self.nrj -= self.nrj_consum
        self.nrj = min(self.nrj_max, self.nrj)
        self.life_expect -= 1
        if self.nrj <= 0 or self.life_expect <= 0:
            self.die()
    
    def is_dead(self):
        return self.speed <= 0

    def disappear(self):
        self.model.visible = False
        del self.model

        

            
##############################################################################

class Zebra(Animal):
    def __init__(self,dna):
        Animal.__init__(self,dna)
        self.model.color =(color.blue)
        
    def move(self, mat, popzebras):
        # Look for point with most food
        best_point = [-1,-1]
        best_point_quality = 0
        for i in range(self.pos[0]-self.vision, self.pos[0]+self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]+self.vision):
                if i >= 0 and i < SIZE_AFRICA and \
                    j >= 0 and j < SIZE_AFRICA:
                    if mat[i][j] > best_point_quality:
                        best_point = [i,j]
                        best_point_quality = mat[i][j]
        # Move toward this point
        # TODO flee tiger
        # TODO flee waste
        if best_point == [-1,-1]:
            # Random move
            best_point= [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        moved = 0
        while moved <= self.speed:
            if self.pos[0] < best_point[0]:
                self.move_model(+1, 0)
                self.pos[0] += 1
            if self.pos[0] > best_point[0]:
                self.move_model(-1, 0)
                self.pos[0] -= 1
            if self.pos[1] < best_point[1]:
                self.move_model(0, +1)
                self.pos[1] += 1
            if self.pos[1] > best_point[1]:
                self.move_model(0, -1)
                self.pos[1] -= 1
            self.model.pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF, 5)
            moved += 1

        # Stay in an empty space
        while self.is_alone(popzebras) == False:
            movx = randint(-1,1) # Random move between -1, 0, or 1
            movy = randint(-1,1)
            self.pos[0] += movx
            self.pos[1] += movy
            self.move_model(movx, movy)
            self.model.pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF, 5)
            

    def is_alone(self, popzebras):
        samepos = 0
        for zeb in popzebras:
            if self.pos == zeb.pos:
                samepos +=1
        return True if samepos == 1 else False
                    
        

    def eat(self, mat_food, mat_waste, dict_resources):
        i, j = self.pos[0], self.pos[1]
        if mat_food[i][j] > 0:
            eaten = min(mat_food[i][j], self.food_eaten)
            mat_food[i][j] -= eaten
            mat_waste[i][j] += eaten
            self.nrj += eaten
            dict_resources[(i, j)].axis -= (0,0,eaten)
            if mat_food[i][j] <= 0:
                dict_resources[(i, j)].visible = False
                del dict_resources[(i, j)]

    def die(self):
        # When a zebra dies, it stops moving but stays as food for tigers
        self.speed = -1
        self.model.color = color.black
        self.nrj = 10

    def clean(self):
        # TODO find better name
        if self.nrj <= 0:
            self.disappear()
            return True
				

##############################################################################

class Tiger(Animal):
    def __init__(self,dna):
        Animal.__init__(self,dna)
        self.model.color=color.red
    
    def move(self, popzebras, poptigers):
        # Look for point with most food
        best_point = [-1,-1]
        for i in range(self.pos[0]-self.vision, self.pos[0]+self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]+self.vision):
                for zeb in popzebras:
                    if [i, j] == zeb.pos:
                        best_point = [i,j]
                        break
        # Move toward this point
        # TODO if several zebras in sigth, choose one randomly (or closest)
        if best_point == [-1,-1]:
            # Random move
            best_point= [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        moved = 0
        while moved <= self.speed:
            if self.pos[0] < best_point[0]:
                self.move_model(1, 0)
                self.pos[0] += 1
            if self.pos[0] > best_point[0]:
                self.move_model(-1, 0)
                self.pos[0] -= 1
            if self.pos[1] < best_point[1]:
                self.move_model(0, 1)
                self.pos[1] += 1
            if self.pos[1] > best_point[1]:
                self.move_model(0, -1)
                self.pos[1] -= 1
            self.model.pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF, 5)
            moved += 1

        # Stay in an empty space
        while self.is_alone(poptigers) == False:
            movx = randint(-1,1) # Random move between -1, 0, or 1
            movy = randint(-1,1)
            self.pos[0] += movx
            self.pos[1] += movy
            self.move_model(movx, movy)
            self.model.pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF, 5)

    def is_alone(self, poptigers):
        samepos = 0
        for tig in poptigers:
            if self.pos == tig.pos:
                samepos +=1
        return True if samepos == 1 else False


    def eat(self, popzebras):
        for zeb in popzebras:
            if self.pos == zeb.pos:
                zeb.die()
                eaten = min(self.food_eaten, zeb.nrj)
                zeb.nrj -= eaten
                self.nrj += eaten
                break;


    def die(self):
        # TODO When a tiger dies, transform in waste
        self.speed = -1
        self.nrj = -1
        self.disappear()
