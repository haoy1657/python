# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:15:54 2021

@author: mehdi
"""

# Racines d'un polynomes du 2dn degrés 

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace (-10 , 10 , 100 , endpoint = True)


# def power_up () : 
#     global X
#     X = np.ones(len(x)) # Matrice ligne 
#     for i in range(0,len(x)) : 
#         X[i] = x [i]**2 # Chaque element au carré 

    
# Au carré
X = x**2 # le ** n'est pas valable sur des 'list'


def delta(a,b,c) : 
    global delta # pour etre traitée hors fonction 
    delta = b**2 - 4*a*c 
    print("le discriminent vaut :", delta)


def racines(d,e,f) : 
    
    #power_up() 
    
    
    # Tracé 
    P = np.ones(len(x))
    for k in range(0,len(x)):
        P[k] = d*X[k] + e*x[k] + f
  
    plt.plot(x,P)
    plt.grid() 
    plt.axis([-5, 5, -10, 10])

    
    delta(d,e,f)


    if delta  < 0 : 
        R1 = np.round((-e - np.sqrt(np.abs(delta))*1j ) / (2*d),1)
        R2 = np.round((-e + np.sqrt(np.abs(delta))*1j ) / (2*d),1)
       
        print("Il ya deux racines complexes qui sont :", R1 ,"&", R2)
    
    
    if delta == 0 : 
        R = np.round((-e)/(2*d),1)
        print("Une racine reélle qui est :", R)
    
    
    if delta > 0 :  
        r1 = round((-e - np.sqrt(delta)) / (2*d),1)
        r2 = round((-e + np.sqrt(delta)) / (2*d),1)
        print("Il y a deux racines réelles qui sont :", r1 ,"&", r2)