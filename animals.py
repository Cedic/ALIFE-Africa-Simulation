# Import
from random import randint
from constants import *
from visual import * 
import Image

# Functions
def dna_to_int(dna):
    return int("".join(str(i) for i in dna), 2)


def random_dna():
	dna = []
	for i in range(4):
		dna.append(randint(0,1))
	return dna


	
# Texture definition

#~ tiger0000_img= Image.open('img/tiger0000.png')
#~ tiger0000 = materials.texture(data=tiger0000_img)
#~ 
#~ tiger0001_img= Image.open('img/tiger0001.png')
#~ tiger0001 = materials.texture(data=tiger0001_img)
#~ 
#~ tiger0002_img= Image.open('img/tiger0002.png')
#~ tiger0002 = materials.texture(data=tiger0002_img)
#~ 
#~ tiger0003_img= Image.open('img/tiger0003.png')
#~ tiger0003 = materials.texture(data=tiger0003_img)
#~ 
#~ tiger0004_img= Image.open('img/tiger0004.png')
#~ tiger0004 = materials.texture(data=tiger0004_img)
#~ 
#~ tiger0005_img= Image.open('img/tiger0005.png')
#~ tiger0005 = materials.texture(data=tiger0005_img)
#~ 
#~ tiger0006_img= Image.open('img/tiger0006.png')
#~ tiger0006 = materials.texture(data=tiger0006_img)
#~ 
#~ tiger0007_img= Image.open('img/tiger0007.png')
#~ tiger0007 = materials.texture(data=tiger0007_img)
#~ 
#~ tiger0008_img= Image.open('img/tiger0008.png')
#~ tiger0008 = materials.texture(data=tiger0008_img)
#~ 
#~ tiger0009_img= Image.open('img/tiger0009.png')
#~ tiger0009 = materials.texture(data=tiger0009_img)
#~ 
#~ tiger0010_img= Image.open('img/tiger0010.png')
#~ tiger0010 = materials.texture(data=tiger0010_img)
#~ 
#~ tiger0011_img= Image.open('img/tiger011.png')
#~ tiger0011 = materials.texture(data=tiger0011_img)
#~ 
#~ tiger0012_img= Image.open('img/tiger0012.png')
#~ tiger0012 = materials.texture(data=tiger0012_img)
#~ 
#~ tiger0013_img= Image.open('img/tiger0013.png')
#~ tiger0013 = materials.texture(data=tiger0013_img)
#~ 
#~ tiger0014_img= Image.open('img/tiger0014.png')
#~ tiger0014 = materials.texture(data=tiger0014_img)
#~ 
#~ tiger0015_img= Image.open('img/tiger0015.png')
#~ tiger0015 = materials.texture(data=tiger0015_img)
#~ 
#~ zebra0000_img= Image.open('img/zebra0000.png')
#~ zebra0000_tex = materials.texture(data=zebra0000_img)
#~ 
#~ zebra0001_img= Image.open('img/zebra0001.png')
#~ zebra0001_tex = materials.texture(data=zebra0001_img)
#~ 
#~ zebra0002_img= Image.open('img/zebra0002.png')
#~ zebra0002_tex = materials.texture(data=zebra0002_img)
#~ 
#~ zebra0003_img= Image.open('img/zebra0003.png')
#~ zebra0003_tex = materials.texture(data=zebra0003_img)
#~ 
#~ zebra0004_img= Image.open('img/zebra0004.png')
#~ zebra0004_tex = materials.texture(data=zebra0004_img)
#~ 
#~ zebra0005_img= Image.open('img/zebra0005.png')
#~ zebra0005_tex = materials.texture(data=zebra0005_img)
#~ 
#~ zebra0006_img= Image.open('img/zebra0006.png')
#~ zebra0006_tex = materials.texture(data=zebra0006_img)
#~ 
#~ zebra0007_img= Image.open('img/zebra0007.png')
#~ zebra0007_tex = materials.texture(data=zebra0007_img)
#~ 
#~ zebra0008_img= Image.open('img/zebra0008.png')
#~ zebra0008_tex = materials.texture(data=zebra0008_img)
#~ 
#~ zebra0009_img= Image.open('img/zebra0009.png')
#~ zebra0009_tex = materials.texture(data=zebra0009_img)
#~ 
#~ zebra0010_img= Image.open('img/zebra0010.png')
#~ zebra0010_tex = materials.texture(data=zebra0010_img)
#~ 
#~ zebra0011_img= Image.open('img/zebra011.png')
#~ zebra0011_tex = materials.texture(data=zebra0011_img)
#~ 
#~ zebra0012_img= Image.open('img/zebra0012.png')
#~ zebra0012_tex = materials.texture(data=zebra0012_img)
#~ 
#~ zebra0013_img= Image.open('img/zebra0013.png')
#~ zebra0013_tex = materials.texture(data=zebra0013_img)
#~ 
#~ zebra0014_img= Image.open('img/zebra0014.png')
#~ zebra0014_tex = materials.texture(data=zebra0014_img)
#~ 
#~ zebra0015_img= Image.open('img/zebra0015.png')
#~ zebra0015_tex = materials.texture(data=zebra0015_img)

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
            
##############################################################################

class Zebra(Animal):
    def __init__(self,dna):
        Animal.__init__(self,dna)
        self.model.color =(color.blue)
    def move(self, mat):
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
        # TODO avoid 2 zebras in same point
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
    def __init__(self,dna):
        Animal.__init__(self,dna)
        self.model.color=color.red
    
    def move(self, popzebras):
        # Look for point with most food
        best_point = [-1,-1]
        for i in range(self.pos[0]-self.vision, self.pos[0]+self.vision):
            for j in range(self.pos[1]-self.vision, self.pos[1]+self.vision):
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
            moved += 1

    def eat(self, popzebras):
        for zeb in popzebras:
            if self.pos == zeb.pos:
                zeb.die()
                eaten = min(self.food_eaten, zeb.nrj)
                zeb.nrj -= eaten
                self.nrj += eaten 
