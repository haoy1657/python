# -*- coding: utf-8 -*-

import datetime


# I/ 
class Personnages : 
    def __init__(self ,prenom,nom) : # Methode init 
        self.nom = nom # On préfixe l'attribut pour dire qu'il appartient à 
        # notre instance 
        self.prenom = prenom 
        # Role du constructeur == Initialiser les attributs
    
    def afficher(self) : # Methode Afficher
        print("Vous vous appelez" , self.nom , self.prenom)
        

# Creation d'un objet 

Naruto = Personnages("Naruto","Uzumaki") 
# Le self correspond à notre instance (Naruto)


# Appel de la methode afficher à partir de l'objet 
"""Naruto.afficher() """


# Modification des données : 
"""Naruto.nom = "Pierre"
Naruto.afficher() """


# II / 

class Vehicules : 
    def __init__(self,marque,annee) : 
        self.marque = marque 
        self.annee = annee 
    def afficher(self) : 
        print("Vehicule de marque" , self.marque)
    def Calculer_age(self) : 
        now = datetime.datetime.now()
        age = now.year - self.annee 
        return age 
        
Ferrari = Vehicules("Ferrari",1977) # Creation d'un objet 

Ferrari.afficher() # Appel de methode à partir de l'objet 
print("Le vehicule a {} ans" .format( Ferrari.Calculer_age())  )


# Modification de données  : 
    
print("\n") ; print("Et maintenant en modifiant les données")

Ferrari.annee = 10 # Modification de l'attribut de l'objet 
Ferrari.afficher() # Appel de methode à partir de l'objet 
print("Le vehicule a {} ans" .format( Ferrari.Calculer_age())  )

# Absurde  , pour cela on utilise les principes d'encaplsulation pour proteger les
# donnees 

# Le caractère privé d'une methode ou d'un attribut avec '__' 

class Voitures : 
    def __init__(self,marque,annee) : 
        self.marque = marque 
        self.__annee = annee  # L'attribut année est privé 
    def afficher(self) : 
        print("Vehicule de marque" , self.marque)
    def Calculer_age(self) : 
        now = datetime.datetime.now()
        age = now.year - self.__annee 
        return age


print("\n") ; print("Avec L'année en attribut privé ")       

Ford = Voitures("Ford", 2004)
#‗  Avec print(Ford.annee) , on obtiendra l'erreur suivante : 
#  Voitures' object has no attribute 'annee'  
# Plus aucun acces en lecture ou en ecriture à l'attribut annee 

""" Si l'on veut donner la possibilité à l'utilisateur de modifier cet attribut , 
on utilise les getters et setters  """ 

# Getters == acces en lecture (@property)
# Setters == Acces controlé en ecriture (@attribut.setter)


class Cars : 
     def __init__(self,marque,annee) : 
         self.marque = marque 
         self.annee = annee  # L'attribut sera mis en privé une fois le setter appelé
     
     @property
     def annee(self) : 
         return self.__annee  # Lecture 
        
     @annee.setter  # Ecriture controllée pour assurer une date coherente 
     def annee (self,annee) : 
            if 1900 < annee <= 2021: 
                self.__annee = annee
                
            elif annee < 1900 and annee > 2021:
                print("no")
                
     
     
     
     def Affichage(self) : 
             print("Vehicule de marque" , self.marque)
         
     def Calculer_age(self) : 
             now = datetime.datetime.now()
             age = now.year - self.annee 
             return str(age)+  " ans"
       
        
        
        
Mustang = Cars("Ford Mustang" , 1976)    
"""Mustang.Affichage() 

 Modifier les donnees"""

print(Mustang.Calculer_age()) # Ligne de code non prise en compte puisqu'elle ne respecte pas
# le critere d'annee défini dans le code de la classe 


# print(Mustang.annee)
        

# Mustang.annee = 2016 # Prise en compte 
# print(Mustang.annee) 
        

        
        
        
        
        
        
        
