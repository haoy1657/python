# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:40:11 2021

@author: mehdi
"""

class Polynomes :
    
  def __init__(self , coef):
        self.__coef = coef
        
  @property
  def coef(self) : return self.__coef  # Lecture
  @coef.setter  # Ecriture controlé pour assurer que l'utilisateur entre bien une liste  
  def coef (self,coef) : 
      if type(coef) == list: 
          self.__coef = coef
      else : raise Exception ("Ce n'est pas un polynome")
  
  
  def getdegre (self) : 
      c = self.__coef 
      return c.index(c[-1]) + 1
 
    
  def getvaleur(self,x) :  
      c = self.__coef 
      return  sum ( [ c[i]*x**(i) for i in range(len(c)) ] ) 

      
  def getderivee (self,x) :
      pol = self.__coef[::-1]
      return  sum ( [ i*(pol[i] )*x**(i-1) for i in range(len(self.__coef)) ][::-1] ) 
     
         
  
  def __eq__ (self,other) : 
      
      # 1/ On commence par verifier que other est un MaClasse
      
      if not isinstance ( other , Polynomes  ) :
          return False
      
      # 2/ Meme adresse => meme objet
      
      if ( self is other ) :
          return True
      
      # Si on arrive ici , c'est qu 'on a un objet de type MaClasse

    # 3/ On compare les champs d'interet
    # Egalite d'attribut
      
      if len(self.__coef ) != len(other.coef) : return False 
      for i in range(len(self.Elements )) : 
            if self.__coef[i] != other.coef[i] : return False 
      return True 
        
  
  def __str__(self) : 
      
      pol = self.__coef ; L = len(self.__coef)
      return str(print( ' + '.join( ("("+str(pol[i])+"x^"+str(i)+")") for i in range(L-1,0,-1) ) , self.__coef[0] ,sep= ' + ')) 
      


# note : la classe == Polynomes
# L'objet == Polynome 
# Les attributs ==> elements composants le polynome 
# other est un objet 
      

Polynome = Polynomes([0.0714 , 0.0714 , - 0.9286 , -0.0714 , 0.8571 ][::-1])
print(Polynome)
 


class Solveur : 
    
      def __init__(self,Polynome, precision):
        self.Polynome , self.__precision = Polynome, precision 
        
        
      def dichotomie(self,xMin, xMax) : 
          
          
        
            pA = Polynome.getvaleur(xMin) ; pB =  Polynome.getvaleur(xMax)
        
            if pA == 0 :  return xMin # si xmin est deja le zéro du polynome
            elif pB== 0 : return xMax # si la borne Xmax est le zero de p 
        
            c = (xMin + xMax) / 2 # Milieu de l'intervalle de dichotomie 
            pC = Polynome.getvaleur(c)  # Initialisation 
        
        # Debut du while  
        
            while pC != 0 and (abs(xMax - xMin) > self.__precision ) : 
            
                c = (xMin + xMax) / 2 
                pC = Polynome.getvaleur(c)
                if pA*pC < 0 : 
                    xMax = c 
                    pB = pC 
                
                else : 
                    xMin = c 
                    pA = pC
        
            return c 
        
      
        
      def newton(self,x0) : 
            
            Un  = self.__precision + 1 
            while Polynome.getvaleur(x0) != 0 and abs(Un) > self.__precision : 
                 
                 Un =   ( Polynome.getvaleur(x0) ) / ( Polynome.getderivee(x0) )
                 x0 =  x0 - Un
            return x0 




#print("Polynome d'orde" , Polynome.getdegre())
#Polynome.getvaleur(-1)  

Solve = Solveur(Polynome,1e-5)


#print(Solve.dichotomie(2,4)) # Okay
#print(Solve.newton(2)) 






""" Tests 


Others = Polynomes([0.0714 , 0.0714 , - 0.9286 , -0.0714 , 0.8571])
print(Polynome == Others )


Others2 = Polynomes([0.0714 , 0.0714 , - 0.9286 , -0.0714 , 0.8571][::-1])
print(Polynome == Others2)

Others3 = Polynomes([0.0714 , 0.0714 , - 0.9286])
print(Polynome == Others3)


print(Polynome.getvaleur(1))
print(Polynome.getderivee(-1))
print(Polynome.getdegre()) """