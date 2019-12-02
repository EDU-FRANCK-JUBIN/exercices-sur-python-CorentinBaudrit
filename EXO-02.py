# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:32:40 2019

@author: Corentin
"""

def diviseursPropres(n):
    div = []
    i = 2
    while i < n:
        if n % i == 0:
            div.append(i)
        i+=1
    if len(div)>0:
        print("Diviseurs propres :", div)
    else:
        print("Pas de diviseur propre pour :", n)
    
def main():
    entierPos = int(input("Entrez un Entier Strictement Positif :"))
    diviseursPropres(entierPos)

main()