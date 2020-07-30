# -*- coding: utf-8 -*-=
"""
Created on Sat Mar 14 10:24:38 2020

@author: Matija
"""

from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import time
def find_image(world, patch):
    
    xSize, ySize = world.size


    world = np.atleast_3d(world)
    patch = np.atleast_3d(patch)
    H, W, D = world.shape[:3]
    h, w, d = patch.shape[:3]

    worldSum = world.cumsum(1).cumsum(0)
    iA, iB, iC, iD = worldSum[:-h, :-w], worldSum[:-h, w:], worldSum[h:, :-w], worldSum[h:, w:] 
    lookupTable = iD - iB - iC + iA

    patchSum = np.array([patch[:, :, i].sum() for i in range(D)])
    possible_match = np.where(np.logical_and.reduce([lookupTable[..., i] == patchSum[i] for i in range(D)]))
    print(possible_match)
    for y, x in zip(*possible_match):
        if np.all(world[y+1:y+h+1, x+1:x+w+1] == patch):
            return (y+1, x+1)

    return ySize//2, xSize//2
    
    
if __name__ == "__main__":

    
    maps = "C:/Users/Matija/Desktop/PSIML/z4/set/map.png"

    """
    N = int(input()) # 1000
    sizeWidth, sizeHeight = map(int, input().split()) # 40 20 
    for i in range(N):
        patch = str(input())
        print(N, sizeHeight, sizeWidth, patch)
    
    """

    world = Image.open(maps)
    xWorld, yWorld = worldSize = world.size
#    print(world,worldSize)

    fig, ax = plt.subplots()
    plt.imshow(world)
    plt.show()
    N = 1000
    sizeWidth, sizeHeight = 40, 40
    with open('C:/Users/Matija/Desktop/PSIML/z4/inputs/2.txt') as f:
        lines_after_header = f.readlines()[3:]
    i = 1
    for line in lines_after_header:
        path = maps[:-8] + line[15:-1] # change int path = input()
        
        patch = Image.open (path)    
        y,x = find_image(world, patch)
#        print(x,y)

        i += 1

    print(i)  

    for j in range(i):
        print(xWorld, yWorld)

    