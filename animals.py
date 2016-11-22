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


	
#~ # Texture definition
 #~ 
tiger1_img= Image.open('img/tiger1.png')
tiger1 = materials.texture(data=tiger1_img)

tiger2_img= Image.open('img/tiger2.png')
tiger2 = materials.texture(data=tiger2_img)

tiger3_img= Image.open('img/tiger3.png')
tiger3 = materials.texture(data=tiger3_img)

tiger4_img= Image.open('img/tiger4.png')
tiger4 = materials.texture(data=tiger4_img)

tiger5_img= Image.open('img/tiger5.png')
tiger5 = materials.texture(data=tiger5_img)

tiger6_img= Image.open('img/tiger6.png')
tiger6 = materials.texture(data=tiger6_img)

tiger7_img= Image.open('img/tiger7.png')
tiger7 = materials.texture(data=tiger7_img)

tiger8_img= Image.open('img/tiger8.png')
tiger8 = materials.texture(data=tiger8_img)

tiger9_img= Image.open('img/tiger9.png')
tiger9 = materials.texture(data=tiger9_img)

tiger10_img= Image.open('img/tiger10.png')
tiger10 = materials.texture(data=tiger10_img)

tiger11_img= Image.open('img/tiger11.png')
tiger11 = materials.texture(data=tiger11_img)

tiger12_img= Image.open('img/tiger12.png')
tiger12 = materials.texture(data=tiger12_img)

tiger13_img= Image.open('img/tiger13.png')
tiger13 = materials.texture(data=tiger13_img)

tiger14_img= Image.open('img/tiger14.png')
tiger14 = materials.texture(data=tiger14_img)

tiger15_img= Image.open('img/tiger15.png')
tiger15 = materials.texture(data=tiger15_img)

zebra1_img= Image.open('img/zebra1.png')
zebra1_tex = materials.texture(data=zebra1_img)

zebra2_img= Image.open('img/zebra2.png')
zebra2_tex = materials.texture(data=zebra2_img)

zebra3_img= Image.open('img/zebra3.png')
zebra3_tex = materials.texture(data=zebra3_img)

zebra4_img= Image.open('img/zebra4.png')
zebra4_tex = materials.texture(data=zebra4_img)

zebra5_img= Image.open('img/zebra5.png')
zebra5_tex = materials.texture(data=zebra5_img)

zebra6_img= Image.open('img/zebra6.png')
zebra6_tex = materials.texture(data=zebra6_img)

zebra7_img= Image.open('img/zebra7.png')
zebra7_tex = materials.texture(data=zebra7_img)

zebra8_img= Image.open('img/zebra8.png')
zebra8_tex = materials.texture(data=zebra8_img)

zebra9_img= Image.open('img/zebra9.png')
zebra9_tex = materials.texture(data=zebra9_img)

zebra10_img= Image.open('img/zebra10.png')
zebra10_tex = materials.texture(data=zebra10_img)

zebra11_img= Image.open('img/zebra11.png')
zebra11_tex = materials.texture(data=zebra11_img)

zebra12_img= Image.open('img/zebra12.png')
zebra12_tex = materials.texture(data=zebra12_img)

zebra13_img= Image.open('img/zebra13.png')
zebra13_tex = materials.texture(data=zebra13_img)

zebra14_img= Image.open('img/zebra14.png')
zebra14_tex = materials.texture(data=zebra14_img)

zebra15_img= Image.open('img/zebra15.png')
zebra15_tex = materials.texture(data=zebra15_img)

textures_zebra = {}
textures_zebra[1] = zebra1_tex
textures_zebra[2] = zebra2_tex
textures_zebra[3] = zebra3_tex
textures_zebra[4] = zebra4_tex
textures_zebra[5] = zebra5_tex
textures_zebra[6] = zebra6_tex
textures_zebra[7] = zebra7_tex
textures_zebra[8] = zebra8_tex
textures_zebra[9] = zebra9_tex
textures_zebra[10] = zebra10_tex
textures_zebra[11] = zebra11_tex
textures_zebra[12] = zebra12_tex
textures_zebra[13] = zebra13_tex
textures_zebra[14] = zebra14_tex
textures_zebra[15] = zebra15_tex

textures_tiger = {}
textures_tiger[1] = tiger1_tex
textures_tiger[2] = tiger2_tex
textures_tiger[3] = tiger3_tex
textures_tiger[4] = tiger4_tex
textures_tiger[5] = tiger5_tex
textures_tiger[6] = tiger6_tex
textures_tiger[7] = tiger7_tex
textures_tiger[8] = tiger8_tex
textures_tiger[9] = tiger9_tex
textures_tiger[10] = tiger10_tex
textures_tiger[11] = tiger11_tex
textures_tiger[12] = tiger12_tex
textures_tiger[13] = tiger13_tex
textures_tiger[14] = tiger14_tex
textures_tiger[15] = tiger15_tex

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
