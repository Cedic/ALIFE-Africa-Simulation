# Import
from random import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
MAT_SIZE = 40
CENTROS_RECURSOS = [[2,38],[37,2]]


# Func
def generar_mat(size):
    mat = []
    for i in range(MAT_SIZE):
        mat.append([0])
        for j in range(MAT_SIZE):
            mat[i].append(0)
    return mat
 
 
def calc_cantidad(num):
    if random() > 0.5:
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
        
    
def generar_recursos(mat, puntos):

    for pt in puntos:
        x = pt[0]
        y = pt[1]
        mat[x][y] = calc_cantidad(50)
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if [i,j] != [x,y]:
                    mat[i][j] = calc_cantidad(45)
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                if mat[i][j] == 0:
                    mat[i][j] = calc_cantidad(35)
        for i in range(x-3,x+4):
            for j in range(y-3,y+4):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat[i][j] = calc_cantidad(20)
        for i in range(x-4,x+5):
            for j in range(y-4,y+5):
                if inmat(i,j,mat):
                    if mat[i][j] == 0:
                        mat[i][j] = calc_cantidad(5)

        
    return mat


def printtab(tab):
    # for i in range(len(tab)):
    #     print("")
    #     for j in range(len(tab[i])):
    #         print(tab[i][j], end="")
    #         if tab[i][j] < 10:
    #             print(" ", end="")
    # print("")

    # Display
    im = plt.imshow(tab, extent=[-1,1,-1,1], interpolation='none');
    plt.xticks([]); plt.yticks([]);
    plt.show()
    
    
matriz = generar_mat(MAT_SIZE)
matriz = generar_recursos(matriz, CENTROS_RECURSOS)

printtab(matriz)

