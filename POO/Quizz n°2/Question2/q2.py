# -*- coding: utf-8 -*-

""" Qu'affiche le code suivant ? """

class A:
    def m1( self, other) :
        if isinstance(other,A):     print("A.m1 avec A")
        elif isinstance(other,B):   print("A.m1 avec B")
        else:                       print("A.m1 avec Autre")

class B:
    def m1( self, other) :
        if isinstance(other,B):     print("B.m1 avec B")
        elif isinstance(other,C):   print("B.m1 avec C")
        else:                       print("B.m1 avec Autre")

class C(B):
    def m1( self, other) :
        if isinstance(other,C):     print("C.m1 avec C")
        if isinstance(other,B):   print("C.m1 avec B")
        else:                       print("C.m1 avec Autre")
        
vA, vB, vC = A( ), B( ), C( )



vA.m1(vA);  vA.m1(vB);  vA.m1(vC)
vB.m1(vA);  vB.m1(vB);  vB.m1(vC)
vC.m1(vA);  vC.m1(vB);  vC.m1(vC)

""" 1/ vA.m1(vA) affiche  "A.m1 avec A"
  
       vA.m1(vB) affiche  "A.m1 avec B"
       
       vA.m1(vC) affiche   "A.m1 avec B"  # vC est de type B , donc le else n'est jamais exécuté dans A
       
       
    2/  vB.m1(vA) : appel de la méthode m1 de la classe B avec l'objet vB. Affiche "B.m1 avec Autre"
    
        vB.m1(vB) : affiche "B.m1 avec B"
        
        vB.m1(vC) : affiche "B.m1 avec B"
        
    
    3/ vC.m1(vA) : affiche "C.m1 avec Autre"
       
       vC.m1(vB) : affiche "C.m1 avec B"
       
       vC.m1(vC) : affiche "C.m1 avec C" ET "C.m1 avec B" car vC est de type "B" et ce n'est pas un elif ! 
"""
