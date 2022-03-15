# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:57:12 2021

@author: Matija
"""

import numpy as np

if __name__ == "__main__":

#    image_path = input()

    img = "01"
    with open("C:\\Users\\Matija\\Downloads\\public-dataset\\public-dataset\\"+img+".in") as f:
        """
        n, s, t, p = [float(x) for x in next(f).split()]
        array = [[float(x) for x in line.split()] for line in f]
        """
        
        n, s, t, p = input(),input(),input(),input()
        array = np.array(n);        
        for i in range(n):
            Px, Py, Vx, Vy = input(),input(),input(),input()
            array[i] = [Px, Py, Vx, Vy]
        
        t2 = -1
        t3 = -1
        #print(n, s, t, p)
        
        #print(array)
        different_timestamps = set()
        different_timestamps.add(0)
        for particle in array:
            #particle[0] Px
            #particle[1] Py
            #particle[2] Vx
            #particle[3] Vy
            different_timestamps.add( round(particle[0] / particle[2]))
            different_timestamps.add( round(particle[1] / particle[3]))
            
        #print(different_timestamps)
        minimal_sum = -1        
        t1 = -1
        for stamp in different_timestamps:

            temporary_sum = 0
            for particle in array:
                temporary_sum += np.sqrt(
                                    (particle[0] - particle[2] * stamp)**2
                                    +
                                    (particle[1] - particle[3] * stamp)**2
                                    )
            if minimal_sum == -1:
                minimal_sum = temporary_sum
                t1 = stamp                
            if minimal_sum > temporary_sum:
                minimal_sum = temporary_sum
                t1 = stamp                
                
            #print(temporary_sum)


    """
    with open("C:\\Users\\Matija\\Downloads\\public-dataset\\public-dataset\\"+img+".out") as f:
        print(t1, t2, t3)
        t1, t2, t3 = [float(x) for x in next(f).split()]
        print(t1, t2, t3)
    """
    print(t1, t2, t3)