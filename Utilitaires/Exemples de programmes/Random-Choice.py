# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:42:33 2021

@author: mehdi
"""

# Liste Aléatoire 
 
import random 

def choix() : 
  #Tuple :
    classe = ("john" , "robert" , "elise" , "toto" , "francoise")
    y = random.choice(classe)
    return y 