# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:05:40 2019

@author: Corentin
"""

def minMaxMoy(list):
    myMin = list[0]
    myMax = list[0]
    myMoy = 0.
    for i in range(len(list)):
        if myMin > list[i]:
            myMin = list[i]
        if myMax < list[i]:
            myMax = list[i]
        myMoy += list[i]
    myMoy /= len(list)
    myTuple = (myMin,myMax,myMoy)
    print("Minimum, Maximum, Moyenne")
    print(myTuple)
    
liste= []

myLenList = int(input("Entrez taille de la liste:"))

for i in range(0,myLenList):
    e = int(input())
    liste.append(e)
    
minMaxMoy(liste)