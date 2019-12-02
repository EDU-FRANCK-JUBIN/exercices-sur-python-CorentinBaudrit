# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:16:50 2019

@author: Corentin
"""

import math


def coneVolume(h,r): 
    volume = float(math.pi*r*r*(h/3.))
    print(volume, "cm^3")


def main():
    hauteur = float(input("Hauteur ?"))
    rayon = float(input("Rayon ?"))
    
    coneVolume(hauteur,rayon)
    
main()