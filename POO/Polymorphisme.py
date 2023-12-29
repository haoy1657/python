# -*- coding: utf-8 -*-


""" Polymorphisme """

""" Traduit le fait qu'un objet d'une classe fille peut etre utilisé a tout moment comme si il s'agissait d'un 
objet de la classe mère """


# Notes  : 
"""On s'assure que l'autre objet existe (i.e. il n'est pas None) et de meme type que
    l'objet courant (mot clé isinstance)"""





class Un : 
    def f1(self) : 
        print("Un.f1")
        
    def f2(self) : 
        if isinstance (self , Un):  #verifier que self est un MaClasse (Un). isinstance verifie aussi que other != None
            print("Un.f1")
          
        if isinstance (self , Deux):
            print("Deux.f1")
            
    def f3 (self , other): 
        if isinstance (other , Un):
            print("Un.f3(Un)")
          
        elif isinstance (other , Deux):
            print("Un.f3(Deux")
        
        
        
        
        
class Deux (Un) :  # Héritage 
    def f3(self , other) : 
        if isinstance (other , Deux):
            print("Deux.f3( Deux )")
          
        elif isinstance (other , Un):
            print("Deux.f3( Un )")
        
    # Deux peux avoir accés à toutes les méthodes et à tous les attributs publiques de Un
    
    
u = Un () # Objet de la classe Un 

u.f1() # Appel de la méthode f1 , affichera "Un.f1" 

u.f2() #  Affichera Un.f1

print("-------------------------")

d = Deux() 
d.f1() # Affichera Un.f1
d.f2() # Affichera Deux.f1 et Un.f1 car par héritage , tout objet de type Deux est aussi de type Un 
# ==> Cas de Polymorphisme 


print("-------------------------")

u.f3(u) # Other == l'objet u crée a partir de Un . Affichera  Un.f3(Un) 
# Etant donné qu'on utilise l'objet crée avec la classe Un , on fait alors appel a la methode f3 de la classe Un

u.f3(d) # Affichera Un.f3(Un) car d est aussi de type "Un" donc la ligne du elif n'est jamais vraiment exécutée 

print("-------------------------")

d.f3(u) # Cette fois ci on appelle la méthode f3 de la classe Deux 
# Affichera Deux.f3( Un ) seulement car tout objet de la classe Un ne peut pas etre de meme type que les objets
# de sa classe fille , l'inverse est cependant correct 

d.f3(d) # Affichera Deux.f3(Deux) (Heritage , d est de meme type que les objets de "Un")  
 
