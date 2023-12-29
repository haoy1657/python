import os
import pickle
from Personnage import *

class Saver:
    def __init__(self,folder) -> None:
        self.folder = folder
    
        
    def save(self,obj,filename):
        ''' Save the object obj to the file self.folder/filename '''
        filename = os.path.join(self.folder,filename)
        with open(filename, 'wb') as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
        print("Sauvegarde effectué avec succès ")


    def load(self,filename):
        ''' load the save from the file self
        .folder/filename '''
        filename = os.path.join(self.folder,filename)
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def delete(self,filename):
        filename = os.path.join(self.folder,filename)
        os.remove(filename)


    def liste_saves(self):
        '''return a list of all saves file's from self.folder'''
        return [
            file
            for file in os.listdir(self.folder)
            if os.path.isfile(os.path.join(self.folder, file))
        ]
    

class SaverDresseur(Saver):
    def __init__(self, folder) -> None:
        super().__init__(folder)

    def choose_save(self,choix):
        liste_saves = self.liste_saves()
        return self.load(liste_saves[choix ])

    def new_save(self):
        """"Crée une nouvelle sauvegarde dans self.saver"""
        nom = input("Quel est votre nom : ")
        dresseur : Dresseur  = Dresseur(nom)
        print("le professeur mehdi vous offre ces pokemons pour débuter")
        for pokemon in starters:
            print(pokemon)
        self.save(dresseur,dresseur.name)
        return dresseur
    
    def delete_save(self):
        """Supprime une sauvegarde parmis les sauvegardes de self.saver """
        liste_saves = self.liste_saves()
        print("Quel sauvegarde voulez vous supprimer?")
        for j,save in  enumerate(liste_saves) :
            print("{}) {}".format(j+1,save))
    
        while True:
            choix = input()
            try:
                choix = int(choix)
            except:
                print("Ce choix n'existe pas ")           
                continue
            if 0 < choix <= len(liste_saves) : 
                self.delete(liste_saves[choix-1])
                print("La sauvegarde {} a été supprimé".format(liste_saves[choix-1]))
                break
            else:
                print("Ce choix n'existe pas ")           

if __name__ == "__main__":
    Saver