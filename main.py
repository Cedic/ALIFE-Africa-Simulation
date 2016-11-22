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
        
    
def generate_a_resource(mat, x, y, n, dict_resources):
	
	mat[x][y] = calc_quantity(n)
	resource_model = cylinder(pos=(x*VCOEFF,y*VCOEFF,0), axis=(0,0,n),
							 radius=3, material = materials.wood)
	dict_resources[(x,y)] = resource_model
	return mat
	
	
def generate_resources(mat, puntos):

    dict_resources = {}
	
    for pt in puntos:
        x = pt[0]
        y = pt[1]
        mat = generate_a_resource(mat, x, y, 50, dict_resources)
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if [i,j] != [x,y]:
					mat = generate_a_resource(mat, i, j, 45, dict_resources)
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                if mat[i][j] == 0:
                    mat = generate_a_resource(mat, i, j, 35, dict_resources)
        for i in range(x-3,x+4):
            for j in range(y-3,y+4):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat = generate_a_resource(mat, i, j, 20, dict_resources)
        for i in range(x-4,x+5):
            for j in range(y-4,y+5):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat = generate_a_resource(mat, i, j, 5, dict_resources)

        
    return mat, dict_resources


def generate_floor():
	floor = box (pos=(SIZE_AFRICA*VCOEFF/2,SIZE_AFRICA*VCOEFF/2,-10), 
				 length=SIZE_AFRICA*VCOEFF + 10, height=SIZE_AFRICA*VCOEFF +10,
				 width=10, material = materials.marble, color = color.orange)


def main(): 
	# 3D Scene for VPython   
	scene = display(title='Africa',
		 x=0, y=0, width=600, height=600,
		 center = (SIZE_AFRICA*VCOEFF/2, SIZE_AFRICA*VCOEFF/2,70), background=(0,0,0))
	

	# Initialization of the simulation field
	matrix_resources = generate_mat(SIZE_AFRICA)
	matrix_resources, models_resources = generate_resources(matrix_resources, RESOURCES_CENTERS)													  
	matrix_waste = generate_mat(SIZE_AFRICA)
	generate_floor()
	
	# Initialization of populations
	popzebras = []
	poptigers = []
	
	for i in range(15):
		new_zebra = Zebra(random_dna())
		popzebras.append(new_zebra)
	for i in range(15):
		new_tiger = Tiger(random_dna())
		poptigers.append(new_tiger)
	
	count_iteration = 1
	while(1):
		print '################### ITERATION ', count_iteration, ' ########################'
		count_iteration += 1
		print len(popzebras), 'zebras alive'
		print len(poptigers), 'tigers alive' 
		for zebra in popzebras:
			zebra.move(matrix_resources, popzebras)
			zebra.eat(matrix_resources, matrix_waste, models_resources)
			zebra.live()
			if zebra.clean():
				print "Snif snif, a zebra is dead"
				popzebras.remove(zebra)
			
		for tiger in poptigers:
			tiger.move(popzebras, poptigers)
			tiger.eat(popzebras)
			tiger.live()
			if tiger.is_dead():
				print "Snif snif, a tiger is dead"
				poptigers.remove(tiger)
			


main()


