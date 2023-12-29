# -*- coding: utf-8 -*-

# Methode __str__ 

"""Tout objet possede une méthode __str__ qui permet de convertir l'objet en
chaine de caracteres"""

class Two_dim :
    def __init__(self,x,y) : 
        self.x , self.y = x,y
    
P1 = Two_dim (12,-0.5)
print(P1)

# resultat  =  <__main__.Two_dim object at 0x0000023B727B9648>

""" 
main : endroit ou l'objet a ete crée
Two_dim : type de l'objet 
0x0000023B727B9648 : adresse de stockage
"""

# Pour un affichage plus fluide et simple , on utilise __str__ 



class Two_dim :
    def __init__(self,x,y) : 
        self.x , self.y = x,y
    
    def __str__(self) : 
        res = " ( {} , {} )" . format(self.x , self.y) 
        return (res)
    

P1 = Two_dim (12,-0.5)
print(P1)
