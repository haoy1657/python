# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

# Détermination d'un nombre Premier

m = int(input("Choisir un nombre :"))
v = int(0) 
if m == 1 : 
    print("Tricheur ;) ")
    v == 1
for v in range(2,m) : # v allant de 2 à m-1
    if m % v == 0 :  # Si reste de la division egal à 0
# => il ne peut etre premier car divisble par autre chose
# que lui meme 
        print("Il n'est pas premier")
        break 
else : 
    if v != 1 : # v different de 1
        print("Bravo ! ") 