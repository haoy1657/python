from abc import ABC , abstracmethod
from ast import While
from math import exp
from Pokemon import *
from Personnage import *
from Combat import *
import random

from Saver import *

class Mode(ABC) : 
    @abstractmethod
   
    def choisir_dresseur(self):
        """Permet de choisir une dresseur parmis les sauvegardes"""
        liste_saves = self.saver.liste_saves()
        if liste_saves == []:
            print("Il n'existe pas encore de sauvegarde")
            self.dresseur =  self.saver.new_save()
        else:
            print("Choisissez votre sauvegarde")
            i=1
            for save in  liste_saves :
                print("{}) {}".format(i,save))
                i+=1
            print("{}) Créer une nouvelle sauvegarde".format(i))
            i+=1
            print("{}) Supprimer une sauvegarde".format(i))
            i += 1
            print("{}) Quitter".format(i))

            while True:
                choix = input("\n")
                try:
                    choix = int(choix)
                except:
                    print("Ce choix n'existe pas ")           
                    continue

                if 0 < choix <= i: 
                    # Choisire une sauvegarde existante
                    if choix < len(liste_saves) + 1:
                        dresseur =  self.saver.load(liste_saves[choix - 1])
                        return dresseur
                    # Créer une nouvelle sauvegarde
                    elif choix == i - 2 :
                        dresseur =  self.saver.new_save()
                        return dresseur

                    # Supprimer une sauvegarde 
                    elif choix == i - 1:
                        self.saver.delete_save()
                        self.choisir_dresseur()
                        
                        
                    # Quitter
                    elif choix == i:
                        self.mode == False
                        return 
                        
                else :
                    print("Ce choix n'existe pas ")
 
     
class Arene(Mode) :  
    def __init__( self ,saver ) : 
        self.saver = saver
        self.mode = True
        print("-----------------------")
        print("Bienvenue Dans le mode Aracade !")   

        print("Joueur n°1 :") 
        print("1) Choisir des pokemons ")
        print("2) Choisir une sauvegarde")

        J1 = self.choisir_dresseur() 
        print("Joueur n°2 :") 
        print("1) Choisir des pokemons ")
        print("2) Choisir une sauvegarde")
        J2 = self.choisir_dresseur()
        Combat(J1,J2)
            




    def choisir_dresseur(self):
        """Permet de choisir une dresseur parmis les sauvegardes ou en choisissant des pokemons """
        while True :
            choix = input() 
            if choix == "1" :  
                while True:
                    dresseur = self.choisir_pokemons() 
                    if dresseur != None:
                        return dresseur

            elif choix =="2":
                while True:
                    dresseur = super().choisir_dresseur()
                    if dresseur != None:
                        return dresseur
            else:
                print("Ce choix n'existe pas")

    def choisir_pokemons(self):
        nom = input("Choisissez votre nom : ")
        print("Choisissez vos Pokemons")
        for i,p in enumerate(pokemon_database):
            print("{}) {}".format(i,p["Nom"]))
        pokemons = []
        for i in range(3):
            while True :
                choix = input("Pokemon n°{} : ".format(i+1))
                try:
                    choix = int(choix) 
                    p = Pokemon(pokemon_database[choix]["Nom"])
                    pokemons.append(p)
                    break
                except:
                    print("Ce choix n'existe pas")
        return Dresseur(nom,pokemons)


        
 
class Exploration(Mode) :  
    def __init__(self,saver:SaverDresseur) : 
        self.mode = True
        self.saver = saver
        print("-----------------------")
        print("Bienvenue dans le mode exploration !")  
        self.dresseur = self.choisir_dresseur()
        while self.mode:
            print("\n----------------------------------------")
            print("{} que souhaitez vous faire".format(self.dresseur.name))
            print("1) Capturer des pokemons sauvages")
            print("2) Changer de deck")
            print("3) Sauvegarder et retourner au menu principal")

            choix = input()
            if choix == "1":
                pokemonSauvage = self.spawnPokemonSauvage()
                combat = Combat(self.dresseur, pokemonSauvage)
                if combat.winner[0] == 0:
                    for pokemon in self.dresseur.deck:
                        pokemon.xp += 10 + max(0,(pokemonSauvage.niveau-pokemon.niveau)/3)

                    
            elif choix == "2":
                self.dresseur.choisir_deck()
            elif choix == "3":
                self.mode = False
                self.saver.save(self.dresseur,self.dresseur.name)
            else:
                print("Ce choix n'existe pas")
    def choisir_dresseur(self):
        return super().choisir_dresseur()


    


    def spawnPokemonSauvage(self):
        return PokemonSauvage(random.choice(pokemon_database)["Nom"]) 
    
   

