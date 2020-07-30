# -*- coding: utf-8 -*-=
"""
Created on Sat Mar 14 10:24:38 2020

@author: Matija
"""

import json
import numpy as np

def insideRectangle(dot, dimSquare):
    topLeftX, topLeftY, width, height = dimSquare
    
    botRightX = topLeftX + width
    botRightY = topLeftY + height
    x,y = dot
    
#    print(topLeftX, topLeftY)
#    print(x,y)
    if topLeftX < x and x < botRightX and topLeftY < y and y < botRightY:
        return 1
    return 0

if __name__ == "__main__":

    
    bboxesPath = "C:/Users/Matija/Desktop/PSIML/z3/set/8/bboxes.json"
    jointsPath = "C:/Users/Matija/Desktop/PSIML/z3/set/8/joints.json"
    
#    bboxesPath = str(input())
#    jointsPath = str(input()) 
    
    
    with open(bboxesPath) as f:
        bboxesContent = json.load(f)
        frames = bboxesContent['frames']
    
    listOfFramesBoxes = []
    listOfBoxNames = []
    
    firstNumBox = 0; indFirstNumBox = False;
    secondNumBox = 0; indSecondNumBox = False;

    for frame in frames:
        ithFrame = []
        num = frame["frame_index"]
        boxes = frame["bounding_boxes"]
        
        if indFirstNumBox == True and indSecondNumBox == False:
            secondNumBox = num 
            indSecondNumBox = True


        if indFirstNumBox == False:
            firstNumBox = num 
            indFirstNumBox = True
        
        for box in boxes:
            identity = box["identity"]              
            if not(identity in listOfBoxNames):
                listOfBoxNames.append(identity)
                # -1 is numDot, 0 is number of frames with matching
            rectangle = box["bounding_box"]
            x = rectangle["x"] * 800
            y = rectangle["y"] * 600
            w = rectangle["w"] * 800
            h = rectangle["h"] * 600
            ithFrame.append((identity,(x,y,w,h)))
        listOfFramesBoxes.append((num - firstNumBox,ithFrame))
        print(num)
        

    temporaryBox = 0

    listOfFramesJoints = []
    listOfPeopleJoints = []

    firstNumJoint = 0; indFirstNumJoint = False;
    secondNumJoint = 0; indSecondNumJoint = False;

    with open(jointsPath) as f:
        jointsContent = json.load(f)
        frames = jointsContent['frames']
        for frame in frames:
            ithFrame = []
            numFrame = frame["frame_index"]


            if indFirstNumJoint == True and indSecondNumJoint == False:
                secondNumJoint = numFrame 
                indSecondNumJoint = True

            if indFirstNumJoint == False:
                firstNumJoint = numFrame 
                indFirstNumJoint = True



            joints = frame["joints"]

            for joint in joints:
                identityDot = joint["identity"]
                xDot = joint["joint"]["x"] * 800
                yDot = joint["joint"]["y"] * 600
                if not(identityDot in listOfPeopleJoints):
                    listOfPeopleJoints.append(identityDot)
                                        # id of Dot
                ithFrame.append((identityDot,(xDot,yDot)))
            listOfFramesJoints.append((numFrame - firstNumJoint, ithFrame))
            print(numFrame)




    diffBox = secondNumBox - firstNumBox
    diffJoint = secondNumJoint - firstNumJoint
    
#    print(listOfPeopleJoints)
#    print(listOfBoxNames)

    dictMatrix = { key:  {keyB: 0 for keyB in listOfPeopleJoints } for key in listOfBoxNames}


    for boxFrame in listOfFramesBoxes:
        numFrame, boxes = boxFrame

        numFrameJoint, joints = listOfFramesJoints[numFrame // diffJoint]
        
        for box in boxes:
            #print(box)
            identityBox, dimBox = box 
            for joint in joints:
                identityJoint, coordDot = joint
                for elemBox in box:
                    if insideRectangle(coordDot, dimBox) == 1:
                        dictMatrix[identityBox][identityJoint] += 1
                    
                #print(identityBox, identityJoint)
                #print(dictMatrix[identityBox][identityJoint])
                
                #print(matrix[identity])
                #print(dictMatrix[identityBox][identityJoint])
            #print(dictMatrix)

        #if numFrame == 0:                  
        #    break
        
    matrix = np.zeros((len(listOfBoxNames),len(listOfPeopleJoints)))
    row = 0    
    for box in dictMatrix:
#        print(box)
        listJoint = dictMatrix[box]    
        col = 0
        for joint in listJoint:
#            print(joint)
#            print(listJoint[joint])
            matrix[row][col] = listJoint[joint]
            col += 1
        row += 1
#        print(listJoint)

#    print(matrix)
    num = min(len(listOfBoxNames),len(listOfPeopleJoints))
#    print(num)
    usedRow = []
    usedCol = []
#    print(num)
    i = 0
#    print(dictMatrix)

    while i < num:
        row, col = ind = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)

        #if matrix[row][col] == 0:
        #    break

        if not ( (row in usedRow) or (col in usedCol)):
            print(str(listOfPeopleJoints[col]) + ":" + str(listOfBoxNames[row]))
#            print(matrix)    
            usedRow.append(row)
            usedCol.append(col)
            i += 1

        matrix[row][col] = -1
        #print(matrix)
        #print(str(listOfPeopleJoints[col]) + "--" + str(listOfBoxNames[row]))
        #print("######################")            
            
        