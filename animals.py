# Import
from random import randint
from constants import *

# Functions
def dna_to_int(dna):
    return int("".join(str(i) for i in dna), 2)

##############################################################################

# Classes
class Animal:
    def __init__(self, dna):
        self.dna = dna

        self.pos = [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        self.nrj_max = 99
        self.nrj = self.nrj_max/2

        dnaint = dna_to_int(self.dna)
        self.speed = dnaint + 1
        self.vision = dnaint*2 + 1
        self.food_eaten = dnaint/2 + 1
        self.nrj_consum = float(dnaint)/4 + 1

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

    def live(self):
        self.nrj -= self.nrj_consum
        self.nrj = min(self.nrj_max, self.nrj)
            
        
# For random dna:
# self.dna = []
# for i in range(4):
#     self.dna.append(randint(0,1))

##############################################################################

class Zebra(Animal):
    def __init__(self):
        Animal.__init__(self)
        
    def move(self, mat):
        # Look for point with most food
        best_point = [-1,-1]
        best_point_quality = 0
        for i in range(self.pos[0]-self.vision, self.pos[0]-self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]-self.vision):
                if mat[i][j] > best_point_quality:
                    best_point = [i,j]
                    best_point_quality = mat[i][j]
        # Move toward this point
        # TODO avoid 2 zebras in same point
        # TODO flee tiger
        # TODO flee waste
        if best_point == [-1,-1]:
            # Random move
            best_point= [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        moved = 0
        while moved <= self.speed:
            if self.pos[0] < best_point[0]:
                self.pos[0] += 1
            if self.pos[0] > best_point[0]:
                self.pos[0] -= 1
            if self.pos[1] < best_point[1]:
                self.pos[1] += 1
            if self.pos[1] > best_point[1]:
                self.pos[1] -= 1
            moved += 1

    def eat(self, mat_food, mat_waste):
        i, j = self.pos[0], self.pos[0]
        if mat_food[i][j] > 0:
            eaten = min(mat_food[i][j], self.food_eaten)
            mat_food[i][j] -= eaten
            mat_waste[i][j] -= eaten
            self.nrj += eaten

    def die(self):
        # When a zebra dies, it stops moving but stays as food for tigers
        self.speed = 0

##############################################################################

class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self)
    
    def move(self, popzebras):
        # Look for point with most food
        best_point = [-1,-1]
        for i in range(self.pos[0]-self.vision, self.pos[0]-self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]-self.vision):
                for zeb in popzebras:
                    if [i, j] == zeb.pos:
                        best_point = [i,j]
                        break
        # Move toward this point
        # TODO avoid 2 tigers in same point
        if best_point == [-1,-1]:
            # Random move
            best_point= [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        moved = 0
        while moved <= self.speed:
            if self.pos[0] < best_point[0]:
                self.pos[0] += 1
            if self.pos[0] > best_point[0]:
                self.pos[0] -= 1
            if self.pos[1] < best_point[1]:
                self.pos[1] += 1
            if self.pos[1] > best_point[1]:
                self.pos[1] -= 1
            moved += 1

    def eat(self, popzebras):
        for zeb in popzebras:
            if self.pos == zen.pos:
                zeb.die()
                eaten = min(self.food_eaten, zeb.nrj)
                zeb.nrj -= eaten
                self.nrj += eaten 
