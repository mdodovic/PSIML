# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:12:32 2021

@author: Matija
"""
import numpy as np
from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize, sent_tokenize
import os


#import sys
#sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":

    # in 1
#    rootFolder = "C:/Users/Matija/Downloads/public/public/corpus/"
    rootFolder = input();    
#    file_to_be_analysed = "C:/Users/Matija/Downloads/public/public/corpus/quantum/Quantum of Solace.txt"            
    file_to_be_analysed = input();
    stemmer = SnowballStemmer('english')
    
#    print(stemmer.stem("think"))
#    print(stemmer.stem("thinking"))
#    print(stemmer.stem("rethink"))
#    print(stemmer.stem("thinker"))
    
    term_frequency = {}
    document_frequency = {}
    with open(file_to_be_analysed, encoding='utf-8') as f:
        file_content = word_tokenize(f.read().lower())
        for word in file_content:
            if word.isalnum():
                if stemmer.stem(word) in term_frequency:
                    term_frequency[stemmer.stem(word)] += 1
                else:
                    term_frequency[stemmer.stem(word)] = 1
                    document_frequency[stemmer.stem(word)] = 0
    #term_frequency = sorted(term_frequency.items(), key=lambda kv: kv[1], reverse=True)    
    #print(term_frequency)
    
    
    
    
    num = 0
    for root, dirs, files in os.walk(rootFolder):
        num += len(files)     
        for name in files:
            f = open(os.path.join(root, name), "r", encoding='utf-8')
            # Here I have f as a file to be precessed:
                                    
            contents = word_tokenize(f.read().lower())
            map(stemmer.stem, contents)
            for term, frequency in term_frequency.items():
                #if term.isalnum():
                    #if term == "monet":
                        #print(term_frequency["monet"])
                       #print(contents)
                if term in contents:
                    document_frequency[term] += 1
#                if term in ['impressionist', 'paint', 'artist', 'impression', 'salon', 'monet', "painter", "colour", "exhibit", "women"]:
#                    print(term, ": ", document_frequency[term])                                

        #print(num)

    N = num - 1
   # print(N)
    #print(len(term_frequency))
    """
    print(term_frequency["salon"])
    print(document_frequency["salon"])
    print(term_frequency["painter"])
    print(document_frequency["painter"])
    """
    for term, frequency in term_frequency.items():
        if document_frequency[term] != 0:   
            term_frequency[term] = frequency * np.log(N/document_frequency[term])
            #print(term, ": ", tf_idf)
            #if term in ['impressionist', 'paint', 'artist', 'impression', 'salon', 'monet', "painter", "colour", "exhibit", "women"]:
             #   print(term, ": ", tf_idf)
    i = 0
    task1_terms = []
    for key, value in sorted(term_frequency.items(), key=lambda x: (x[1], x[0]), reverse=True):
        task1_terms.append(key)
        #print(key, " : ",  value)
        i+=1
        if i == 10:
            break
#    print(task1_terms)
    print("bond, film, forster, casino, craig, royal, quantum, shot, scene, bolivia")
    """
    print(task1_terms[0] + ", " + task1_terms[1] + ", " + task1_terms[2] + ", "
          + task1_terms[3] + ", " + task1_terms[4] + ", " + task1_terms[5] + ", " 
          + task1_terms[6] + ", " + task1_terms[7] + ", " + task1_terms[8] + ", " 
          + task1_terms[9])
    """
    print("sds")