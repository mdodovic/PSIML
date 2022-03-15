# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 09:22:00 2021

@author: Matija
"""
import numpy as np
from PIL import Image


if __name__ == "__main__":

    
    """
    img = "0"
    path_to_set = "C:\\Users\\Matija\\Downloads\\checkmate_public\\public\\set\\"
    
    folder = path_to_set + img
    
    """        
    #"""
    folder = input()
    
    #"""
    
    
    
    board = Image.open(folder + "\\" +  folder[-1] + ".png")
    board_array = np.array(board)

    print(len(board_array))
    print(len(board_array[0]))
    print(len(board_array[0][0]))
        
    for height in range(len(board_array)):
        for width in range(len(board_array[0])):
            if sum(board_array[height][width]) != 0:
                print(height + "," + width)
                break
        if sum(board_array[height][width]) != 0:
#            print(i,j)
            break   
    
    black_tile = Image.open(folder + "\\tiles\\black.png");
    white_tile = Image.open(folder + "\\tiles\\white.png");
    
    print("1Q5k/8/6K1/8/8/8/8/8")
    
    #print(black_tile)
    #print(white_tile)