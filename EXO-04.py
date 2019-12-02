# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:17:27 2019

@author: Corentin
"""

import random

VALID_CHARS = ['a', 't', 'g', 'c']

#Verification de chain valide
def chain_is_valid(chain):
    chain = chain.lower()
    for c in chain:
        if c not in VALID_CHARS:
            return False
    return (len(chain) > 0)

#generation chaine
def create_chain(len):
    chain = ""
    for i in range(len):
        chain += random.choice(VALID_CHARS)
    print(chain)
    return chain

#recherche sequence
def sequence_in_chain(chain, sequence):
    print(f"""
        Il y a {round((chain.count(sequence) / len(chain)) * 100, 2)}% 
        de "{sequence}" dans votre chaine.
    """)

def main():
    valid = False
    theChain = None
    
    while(valid==False):
        choice = input("Voulez vous générer une chaine (1) ou entrez votre chaine ? (2):")
        if (int(choice) == 1 ):
            valid = True
            lenchaine = input("Veuillez indiquez la longueur de la chaine à générer :")
            theChain =create_chain(int(lenchaine))
        elif (int(choice) == 2):
            valid = True
            valid2 = False
            while (valid2 == False):
                theChain = input("Entrez une Sequence adn composée de t g a c :")
                valid2 = chain_is_valid(theChain)
        else:
            print("Selection non valide veuillez choisir 1 ou 2")
            
    mySeq = input("Entrez une sequence a rechercher :")
    while(chain_is_valid(mySeq) == False):
        mySeq = input("Entrez une sequence a rechercher :")
    sequence_in_chain(theChain, mySeq)
    
main()