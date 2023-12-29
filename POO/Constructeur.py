# -*- coding: utf-8 -*-
class Constructeur : 
    def method1(self):
        print("okay")
        
Objet = Constructeur()
Objet.method1()


class Democonstructeur : 
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
        
    # Methodes 
    def methode2(self) : 
        print("Methode n°2 , a = " , self.a)
        
Objet2 = Democonstructeur(10,11)
Objet2.methode2()

# Un constructeur doit toujours initialiser tous les attributs d'une classe 

# pour mettre à un attribut une valeur par défaut : 
    
class Democonstructeur : 
    def __init__(self,a,b,c=0):
        self.a = a 
        self.b = b 
        self.c = 0 
        
    # Methodes 
    def methode2(self) : 
        print("Methode n°2 , a = " , self.a)
    def methodeC(self) : 
        print("Voici C : " , self.c)
        
        
Objet3 = Democonstructeur(10,11) # Pas de valeurs passée à C , il prendra 0 par defaut 
# comme mentionné plus haut dans le constructeur 
Objet3.methodeC()       

        
        
        
        
        
        
        
