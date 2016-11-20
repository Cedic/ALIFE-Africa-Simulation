# Import
from random import randint

# Functions
def dna_to_int(dna):
    return int("".join(str(i) for i in dna), 2)

# Classes
class Animal:
    def __init__(self, dna):
        self.dna = dna

        self.position = [randint(0,SIZE_AFRICA), randint(0,SIZE_AFRICA)]
        self.nrj_max = 99
        self.nrj = self.nrj_max/2

        dnaint = dna_to_int(self.dna)
        self.speed = dnaint +1
        self.vision = dnaint*2 + 1
        self.food_eaten = dnaint/2 + 1
        self.nrj_consum = float(dnaint)/4 +1

    def alive(self):
        return self.nrj > 0

    def reproduct(self, animal2):
        dim = len(self.position)
        new_dna = []
        fixed_point = randint(0,dim)
        for i in range(dim):
            if i < fixed_point:
                new_dna.append(self.position[i])
            else:
                new_dna.append(animal2.position[i])
        return new_dna
        
# For random dna:
# self.dna = []
# for i in range(4):
#     self.dna.append(randint(0,1))
        

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
        i, j = self.position[0], self.position[0]
        if mat_food[i][j] > 0:
            eaten = min(mat_food[i][j], self.food_eaten)
            mat_food[i][j] -= eaten
            mat_waste[i][j] -= eaten
            self.nrj += eaten

# class Tiger(Animal):
    
