# Import
from random import randint
from constants import *
from visual import * 
from textures import *
import Image
from time import sleep

# Functions
def dna_to_int(dna):
    return int("".join(str(i) for i in dna), 2)


def random_dna():
    dna = []
    for i in range(4):
        dna.append(randint(0,1))
    return dna

def random_pos():
    return [randint(0,SIZE_AFRICA-1), randint(0,SIZE_AFRICA-1)]

def is_neighbour(ani1, ani2):
    if abs(ani1.pos[0] - ani2.pos[0]) <= 2 and \
       abs(ani1.pos[1] - ani2.pos[1]) <= 2:
        return True
    else:
        return False



##############################################################################


# Classes
class Animal:
    def __init__(self, dna, pos):
        self.dna = dna
        self.pos = pos
        self.nrj_max = 250 + randint(-50,50)
        self.nrj = self.nrj_max/2
        self.life_expect = 1000 + randint(-200,200) # In number of iterations
        self.desire = randint(20,50)

        dnaint = dna_to_int(self.dna)
        self.speed = dnaint + 1
        self.vision = dnaint*2 + 1
        self.food_eaten = dnaint/2 + 1
        self.nrj_consum = float(dnaint)/4 + 1
        self.waste_level = 0

        # Graphic model
        self.model = box(pos=(self.pos[0]*VCOEFF - 5, self.pos[1]*VCOEFF -5, 10),
                              length=8, height = 8, width = 8)

    def alive(self):
        return self.nrj > 0

    def reproduct(self, pop):
        libido = self.desire
        child_dna = None
        if self.nrj < self.food_eaten*4:
            libido /= 2
        # TODO penalty on libido if tiger
        for ani in pop:
            if not ani.is_dead():
                if is_neighbour(self, ani):
                    libido += ani.desire
                    libido -= abs(dna_to_int(self.dna) - dna_to_int(ani.dna))*4
                    if libido > 100:
                        self.desire = 0
                        ani.desire = 0
                        child_dna = self.crossover(ani)
                        break
        return child_dna

    def crossover(self, animal2):
        dim = len(self.dna)
        new_dna = []
        fixed_point = randint(0,dim-1)
        for i in range(dim):
            if i < fixed_point:
                new_dna.append(self.dna[i])
            else:
                new_dna.append(animal2.dna[i])
        return new_dna
        
    def move_model(self, x, y):
        for i in range(VCOEFF):
            self.model.pos=(self.pos[0]+x, self.pos[1]+y, 5)

    def live(self):
        self.nrj -= self.nrj_consum
        self.nrj = min(self.nrj_max, self.nrj)
        self.life_expect -= 1
        if self.nrj <= 0 or self.life_expect <= 0:
            self.die()
    
    def make_waste(self, matrix_waste, waste_models):
		if (random.randint(1,35) == 1) and self.waste_level > 0 :
			if (self.pos[0], self.pos[1]) in waste_models.keys():
				waste_models[(self.pos[0], self.pos[1])].axis += (0, 0, self.waste_level/WASTE_SCALE)
			else:
				waste = cone(pos=(self.pos[0]*VCOEFF, self.pos[1]*VCOEFF, 0),
							 axis=(0,0,self.waste_level/WASTE_SCALE), radius = 5,
							 color = color.magenta)
				waste_models[(self.pos[0], self.pos[1])] = waste
			matrix_waste[self.pos[0]][self.pos[1]] += self.waste_level
			self.waste_level = 0
			print 'OHOOOOO IL A FAIT CACA'
			
		
    def is_dead(self):
        return self.speed <= 0

    def disappear(self):
        self.model.visible = False
        del self.model

        

            
##############################################################################

class Zebra(Animal):
    class_counter = 0
    def __init__(self,dna,pos):
        Animal.__init__(self,dna,pos)
        dna = dna_to_int(dna)
        self.death = False
        self.death_by_tiger = False
        self.model.color = color.white
        self.id = Zebra.class_counter
        Zebra.class_counter +=1
        #~ self.model.material=textures_zebra[dna]
        
    def move(self, mat, matwaste, popzebras, poptigers):
        # Look for point with most food
        best_point = [-1,-1]
        best_point_quality = 0
        for i in range(self.pos[0]-self.vision, self.pos[0]+self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]+self.vision):
                if i >= 0 and i < SIZE_AFRICA and \
                    j >= 0 and j < SIZE_AFRICA:
                    current_quality = mat[i][j]
                    # Lower quality if tiger nearby
                    for tig in poptigers:
                        if abs(tig.pos[0] - i <= 2) or \
                           abs(tig.pos[1] - j <= 2):
                            current_quality -= 20
                    # Lower quality if waste nearby
                    waste_near = 0
                    for ii in range(i-2, i+2):
                        for jj in range(j-2, j+2):
                            if ii >= 0 and ii < SIZE_AFRICA and \
                               jj >= 0 and jj < SIZE_AFRICA:
                                waste_near += matwaste[ii][jj]
                    current_quality -= waste_near
                    if current_quality > best_point_quality:
                        best_point = [i,j]
                        best_point_quality = current_quality
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
            mat_food[i][j] -= eaten*3
            self.waste_level += eaten
            self.nrj += eaten
            dict_resources[(i, j)].axis -= (0,0,eaten)
            if i >= 0 and i < SIZE_AFRICA and \
               j >= 0 and j < SIZE_AFRICA:
                if mat_food[i][j] <= 0:
                    mat_food[i][j] = 0
                    dict_resources[(i, j)].visible = False
                    del dict_resources[(i, j)]
            return True
        else:
			return False

    def die(self):
        # When a zebra dies, it stops moving but stays as food for tigers
        if not self.death:
            print 'Snif snif, Zebra ', self.id, ' died.' 
            self.death= True
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
    class_counter=0
    def __init__(self,dna,pos):
        Animal.__init__(self,dna,pos)
        dna = dna_to_int(dna)
        self.model.color = color.orange
        self.id = Tiger.class_counter
        Tiger.class_counter += 1
        
        #~ self.model.material=textures_tiger[dna]
    
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
                if not zeb.death_by_tiger:
                    zeb.death_by_tiger = True
                    print 'Tiger ', self.id, ' just killed Zebra', zeb.id
                eaten = min(self.food_eaten, zeb.nrj)
                self.waste_level += eaten
                zeb.nrj -= eaten
                self.nrj += eaten
                return True
                break;
            return False


    def die(self):
        # TODO When a tiger dies, transform in waste
        print 'Snif snif, Tiger ', self.id, ' died.' 
        self.speed = -1
        self.nrj = -1
        self.disappear()
