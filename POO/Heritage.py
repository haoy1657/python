# -*- coding: utf-8 -*-
#Notions d'heritage 

class A : 
     def __init__ (self , a1 , a2 ) : 
         self.a1 = a1 ; self.a2 = a2 
    
     def __str__ (self) : 
         return ("Affichage de l'objet : {} & {}".format(self.a1 , self.a2))
     
     def methodepublique(self) : 
         print("a1 vaut : {}".format(self.a1))
         self.__methodeprivee()
        
     def __methodeprivee(self) : 
         print("Non appellable depuis l'extérieur :) et a2 vaut {}".format(self.a2))
         
        
# Objet = A(10,11) # Objet de type A en appellant le constructeur de A
# Objet.methodepublique()

# print(Objet) # Coder la méthode str pour afficher les objets est essentiel ! 





""" Ajoutons une classe B héritant de A

class B(A) : 
    pass          # Aucun constructeur n'est défini 

Objet2 = B(20,33)
Objet2.methodepublique() 


A retenir : dans ce cas la , on fait implicitement appel au constructeur de A , la classe mère.
Tout objet B a donc accès aux attributs et methodes publiques de la classe mere

# Modifions un attribut publique de A

Objet2.a1 = 17
Objet2.methodepublique()


Objet2.a2 = 99
Objet2.methodepublique()
"""
# impossible de modifier les attributs privés par contre 



# On ajoute maintenant un constructeur pour B 

class B(A) : 
    
    def __init__(self , a1 , a2 , b1) : 
        
        super().__init__(a1, a2) # Methode super => faire réference à une methode de la classe mère depuis la classe fille
        # C'est en gros , l'appel au constructeur de la classe mère 
        # Super va donc remplacer self dans les appels qu'on a l'habitude de faire 
        
        # L'appel à la fonction mère doit etre la première ligne de la mèthode 
        
        self.b1 = b1 # On gère les nouveaux attributs 
        
# Objet3 = B(1,2,3)


# print(Objet3) 
""" Important : voici ce que donne l'affichage : Affichage de l'objet : 1 & 2 """
""" Il nous faut alors coder dans la classe fille une methode str pour afficher les attributs nouvellement crées 
dans cette classe fille """



class B2(A) : 
    
    def __init__(self , a1 , a2 , b1) : 
        
        super().__init__(a1, a2) 
        self.b1 = b1 
        
    # Méthode ToString propre à la classe fille 
    
    def __str__ (self) : 
        res = super().__str__() # appel de la fonction str de la classe mere pour ne pas perdre les attributs 
        # de cette meme classe mere 
        res = res + " & {})".format(self.b1)
        return res
        
Objet4 = B2(40,2,3)
print(Objet4)



