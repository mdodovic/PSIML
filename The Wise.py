# -*- coding: utf-8 -*-=
"""
Created on Sat Mar 14 10:24:38 2020

@author: Matija
"""

import os
import numpy as np
import re

if __name__ == "__main__":

    #rootFolder = str(input()) 
    rootFolder = "C:/Users/Matija/Downloads/public/public/set/3"

    num = 0
    numCa = 0
    numWpa = 0
    
    numWrongAnswer = 0
    numCorrectAnswer = 0
    numWrongPredicted = 0
    numCorrectPredicted = 0
    
    numUseful = 0
    
    thresholdNominal = 70
    EER = 0.0
    difMin = 1.0
    maxNum = 1000
    ca = np.zeros(maxNum)
    wpaAllThresh = np.zeros((101,maxNum))
    
    
    for root, dirs, files in os.walk(rootFolder):
        
    #   print(len(files))
    #   print((files))
        num += len(files)
        for name in files:
            f = open(os.path.join(root, name), "r")
            contents = f.read()
            index = int(re.search(r'\d+', name).group())


            if name.find('ca') != -1:
                # correct answer            
                if contents == "No":
                    numWrongAnswer += 1
                    ca[index] = -1 # negative answer
                else:
                    numCorrectAnswer += 1
                    ca[index] = 1 # positive answer
                
                numCa += 1
            
            if name.find('wpa') != -1:            
                contents = int(re.search(r'\d+', contents).group())
                # predicted answer
                numWpa += 1
                for threshold in range(0,101,1):
                    if contents >= threshold:
                        wpaAllThresh[threshold][index] = 1 # predicted positive
                    else:
                        wpaAllThresh[threshold][index] = -1 # predicted negative
                    
            
            f.close()

    for threshold in range(0,101,1):
        numWrongAnswerUseful = 0
        numCorrectAnswerUseful = 0
        numTP = 0
        numFP = 0
        numUseful = 0
                
        for i in range(maxNum):
            if ca[i] != 0 and wpaAllThresh[threshold][i] != 0:
                numUseful += 1
                if ca[i] == 1:
                    numCorrectAnswerUseful += 1
                if ca[i] == -1:
                    numWrongAnswerUseful += 1
                    
                if ca[i] == 1 and wpaAllThresh[threshold][i] == 1:
                    numTP += 1
        
                if ca[i] == -1 and wpaAllThresh[threshold][i] == 1:
                    numFP += 1
        
        #TPR = round(numTP/numCorrectAnswerUseful,3)
        #FPR = round(numFP/numWrongAnswerUseful,3)
        TPR = numTP/numCorrectAnswerUseful
        FPR = numFP/numWrongAnswerUseful

        if (abs(FPR - (1-TPR))) < difMin:
            EER = FPR
            difMin = (abs(FPR - (1-TPR)))
        
        if threshold == thresholdNominal:
            output = str(numCorrectAnswer) + "," + str(numWrongAnswer) + "," + str(numUseful) + "," + str(round(TPR,3)) + "," + str(round(FPR,3)) + ","
        #print(str(numCorrectAnswer) + "," + str(numWrongAnswer) + "," + str(numUseful) + "," + str(TPR) + "," + str(FPR) + "," + str(EER))
        
    print(output + str(round(EER,3)))