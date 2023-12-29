# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:27:05 2021

@author: mehdi
"""

""" TP3 avec la methode add """ 


class Polynomes :
    
  def __init__(self , Elements):
        self.Elements = Elements 
  
  def Affiche(self) : 
      
     L=(len(self.Elements )) ; pol = self.Elements 
     res= print( ' + '.join( ("(" + str(pol[i]) + "x^" + str(i) + ")") for i in range(L-1,0,-1) ) , self.Elements[0] ,sep= ' + ')
     return res 
 
  def __add__(self, other):
      
      i = max([len(self.Elements) , len(other.Elements)])
      
      if len(self.Elements) > len(other.Elements) : smaller = other.Elements
      else : smaller = self.Elements
      zero = i - len(smaller)
      for j in range(zero) : smaller.append(0)
      
      return ( [ self.Elements[k] + other.Elements[k] for k in range(i)] )
          
       
      
   


Polynome = Polynomes([1,2,0,4]) 
Polynome.Affiche() 

Autre = Polynomes([1,0,6,4,9,10,1967])
Autre.Affiche() 

print(Polynome + Autre)