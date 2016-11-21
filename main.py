# Import
from random import random
import matplotlib.pyplot as plt
import numpy as np
from visual import * 
from constants import *
import Image
from animals import *

# Func
def generate_mat(size):
    mat = []
    for i in range(SIZE_AFRICA):
        mat.append([0])
        for j in range(SIZE_AFRICA):
            mat[i].append(0)
    return mat
 
 
def calc_quantity(num):
    if random.uniform(0,1) > 0.5:
        num *= 1.2
    else:
        num *= 0.8
    return int(num)
    
    
def inmat(i,j,mat):
    # print(i,j)
    if i < 0 or i >= len(mat):
        # print("False")
        return False
    elif j < 0 or j >= len(mat[0]):
        # print("False")
        return False
    else:
        # print("True")
        return True   
        
    
def generate_a_ressource(mat, x, y, n, dict_ressources):
	
	mat[x][y] = calc_quantity(n)
	ressource_model = cylinder(pos=(x*VCOEFF,y*VCOEFF,0), axis=(0,0,n),
							 radius=3, material = materials.wood)
	dict_ressources[(x,y)] = ressource_model
	return mat
	
	
def generate_ressources(mat, puntos):

    dict_ressources = {}
	
    for pt in puntos:
        x = pt[0]
        y = pt[1]
        mat = generate_a_ressource(mat, x, y, 50, dict_ressources)
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if [i,j] != [x,y]:
					mat = generate_a_ressource(mat, i, j, 45, dict_ressources)
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                if mat[i][j] == 0:
                    mat = generate_a_ressource(mat, i, j, 35, dict_ressources)
        for i in range(x-3,x+4):
            for j in range(y-3,y+4):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat = generate_a_ressource(mat, i, j, 20, dict_ressources)
        for i in range(x-4,x+5):
            for j in range(y-4,y+5):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat = generate_a_ressource(mat, i, j, 5, dict_ressources)

        
    return mat, dict_ressources


def generate_floor():
	floor = box (pos=(SIZE_AFRICA*VCOEFF/2,SIZE_AFRICA*VCOEFF/2,-10), 
				 length=SIZE_AFRICA*VCOEFF + 10, height=SIZE_AFRICA*VCOEFF +10,
				 width=10, material = materials.marble, color = color.orange)

    
scene = display(title='Africa',
     x=0, y=0, width=600, height=600,
     center = (SIZE_AFRICA*VCOEFF/2, SIZE_AFRICA*VCOEFF/2,70), background=(0,0,0))
         
matrix_ressources = generate_mat(SIZE_AFRICA)
matrix_ressources, models_ressources = generate_ressources(matrix_ressources,
													  RESSOURCES_CENTERS)
													  
matrix_pollution = generate_mat(SIZE_AFRICA)



#~ printtab(matriz)
print(models_ressources)
generate_floor()
