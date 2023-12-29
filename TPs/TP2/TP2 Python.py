# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:38:44 2021

@author: Mehdi
"""

""" TP2 Python """ 


# 1  - Get valeur 

def getvaleur (p,x) : 
    
      # Le polynome sera representé par une liste 
      pol = p[::-1]
      return  sum ( [ pol[i]*(x**i) for i in range(len(p)) ][::-1] ) 
  
    
# Get derivée  

def getderivee (p,x) : 
     pol = p[::-1]
     return  sum ( [ i*(pol[i] )*x**(i-1) for i in range(len(p)) ][::-1] ) 
    
    


# Exercice 2 


def dichotomie( p, xMin, xMax, eps ) : 
    
    pA = getvaleur(p, xMin) ; pB =  getvaleur(p, xMax)
    
    if pA == 0 :  return xMin # si xmin est deja le zéro du polynome
    elif pB== 0 : return xMax # si la borne Xmax est le zero de p 
    
    c = (xMin + xMax) / 2 # Milieu de l'intervalle de dichotomie 
    pC = getvaleur(p,c)  # Initialisation 
    
    # Debut du while  
    
    while pC != 0 and (abs(xMax - xMin) > eps ) : 
        
        c = (xMin + xMax) / 2 
        pC = getvaleur(p,c)
        if pA*pC < 0 : 
            xMax = c 
            pB = pC 
            
        else : 
            xMin = c 
            pA = pC
    
    return c 


def newton( p, x0, eps ) : 
    
    Un  = eps + 1 
    while getvaleur(p, x0) != 0 and abs(Un) > eps : 
         
         Un =   ( getvaleur(p, x0) ) / ( getderivee(p, x0) )
         x0 =  x0 - Un
    return x0 



""" Completer le programme principal precedent pour rechercher le zero 
du polynome  p(x) = 0.0714 x**4 +0.0714 x**3 − 0.9286x**2 − 0.0714x + 0.8571
 avec une precision ε = 10−5 par la methode de Newton ( x0 = 2) et
dichotomique (intervalle [2 ; 4]). """ 

p =[0.0714 , 0.0714 , - 0.9286 , -0.0714 , 0.8571 ]
eps = 10e-5
x0 = 2 

# Question 3 

print(dichotomie( p, 2, 4 , eps ))

# print(newton( p, x0, eps ) )


""" Exercice 3""" 
def afficnepolynome(p) : 
 L=(len(p)) ; pol = p[::-1]
 return  print( ' + '.join( ("("+str(pol[i])+"x^"+str(i)+")") for i in range(L-1,0,-1) ) , p[L-1] ,sep= ' + ') 

p =[0.0714 , 0.0714 , - 0.9286 , -0.0714 , 0.8571 ]
afficnepolynome(p)  

    
     # "(" + str(pol[i]) + "x^" + str(i) + ")" 
    # ==> concatenation de chaines de caracteres avec + 
 
 
 # Egalité de deux polynomes 
def egalite_polynomes(a,b) : 
    if len(a) != len(b) : return False 
    else : 
        for i in range(len(a)) : 
            if a[i] != b[i] : return False 
    return True 
  

  

