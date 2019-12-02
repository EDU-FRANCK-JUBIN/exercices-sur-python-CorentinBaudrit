# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:48:04 2019

@author: Corentin
"""

import math

E = math.e


def approxE(n):
    valeurs = []
    if n<=50:
        print("N pas assez grand!")
    else:
        i = 0
        myE = 0
        while i <= n:
            myE += (1/math.factorial(i))
            i+=1
        valeurs.append(myE)
        valeurs.append(myE-E)
        print("Mon exponentielle :", valeurs[0])
        print("Erreur D'approximation :", valeurs[1])

def main():
    e = int(input("Entrez un entier > 50 :"))
    approxE(e)
    
main()