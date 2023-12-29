import csv
import os.path
from random import randint, randrange, uniform
from abc import ABC, abstractmethod, abstractproperty
from typing import List
from Exceptions import *


TYPETAB = {
    'Air':   {'Air': 1,   'Eau': 1,   'Feu': 0.5, 'Terre': 1.5 },
    'Eau':   {'Air': 1.5, 'Eau': 1,   'Feu': 1,   'Terre': 0.5 },
    'Feu':   {'Air': 0.5, 'Eau': 1.5, 'Feu': 1,   'Terre': 1   },
    'Terre': {'Air': 1,   'Eau': 0.5, 'Feu': 1.5, 'Terre': 1   }
}

pokemonDatabaseKeys = set(['Nom', 'Avant', 'Apres', 'Element', 'Niveau', 'Vie', 'Energie', 'Regeneration', 'Resistance', 'Competences'])
attaqueDatabaseKeys = set(['Nom', 'Description', 'Element', 'Puissance', 'Precision', 'Cout'])
defenseDatabaseKeys = set(['Nom', 'Description', 'Element', 'Soin', 'Energie', 'Cout'])

# Extract data as a list of dictionary 
dir = os.path.dirname(__file__) 
with open(os.path.join(dir,'data/pokemon.txt'),encoding='us-ascii'  , newline='') as f: 
    pokemon_database = list(csv.DictReader(f,delimiter='\t')) 
with open(os.path.join(dir,'data/attaque.txt'),encoding='iso-8859-1', newline='') as f: 
    attaque_database = list(csv.DictReader(f,delimiter='\t')) 
with open(os.path.join(dir,'data/defense.txt'),encoding='iso-8859-1', newline='') as f: 
    defense_database = list(csv.DictReader(f,delimiter='\t'))
del dir

# Clean databases by converting elements to the good type 
for p in pokemon_database:
    p["Niveau"] =  [int(x) for x in p["Niveau"].split("-")]
    p["Vie"] =  [int(x) for x in p["Vie"].split("-")]
    p["Energie"] =  [int(x) for x in p["Energie"].split("-")]
    p["Regeneration"] =  [int(x) for x in p["Regeneration"].split("-")]
    p["Resistance"] =  [int(x) for x in p["Resistance"].split("-")]
    p["Competences"] =  p["Competences"][1:-1].split(", ")
    if not pokemonDatabaseKeys.issubset( set(p.keys()))  : raise Exception("DatabaseError")

for attaque in attaque_database: 
    attaque["Puissance"] = int( attaque["Puissance"] )
    attaque["Precision"] = int( attaque["Precision"] )
    attaque["Cout"] = int( attaque["Cout"] )
    if not attaqueDatabaseKeys.issubset( set(attaque.keys()))  : raise Exception("DatabaseError")

for defense in defense_database: 
    if defense["Soin"]!="": defense["Soin"] = [int(x) for x in defense["Soin"].split("-")]
    else : defense["Soin"] = [0,0]
    if defense["Energie"]!="": defense["Energie"] = [int(x) for x in defense["Energie"].split("-")]
    else : defense["Energie"] = [0,0]
    defense["Cout"] = int( defense["Cout"] )
    if not defenseDatabaseKeys.issubset( set(defense.keys()))  : raise Exception("DatabaseError")





class Pokemon :

    def __init__(self,name) -> None:
        self.living = True

        for p in pokemon_database: 
            if p["Nom"] == name :  
                self.data = p 
                break
        if not hasattr(self, 'data'): raise ExistenceError
        self.name = self.data["Nom"]
        self.niveau = self.data["Niveau"][0]
        self.regeneration = self.data["Regeneration"][0]
        self.resistance = self.data["Resistance"][0]
        self.energieMax = self.data["Energie"][0]
        self.energie = self.energieMax
        self.vieMax = self.data["Vie"][0]
        self._vie = self.vieMax
        self.competences : List[Competences] = []
        for c in self.data["Competences"]:
            try : self.competences.append(Attaque(c))
            except ExistenceError : self.competences.append(Defense(c))
        self._xp = 0

    @property
    def vie(self):
        return self._vie
    @vie.setter
    def vie(self,value):
        self._vie = max(0,value)
        if self.vie <= 0:
            self.living = False


    @property
    def xp(self):
        return self._xp
    @xp.setter
    def xp(self,value):
        self._xp = value
        while self._xp >= 100:
            self._lvl_up()
            self._xp -= 100
    
    def _lvl_up(self) :
        if self.niveau < self.data["Niveau"][1]: 
            self.niveau +=1
            self.regeneration = self.data["Regeneration"][0] + \
                int( self.niveau*abs(self.data["Regeneration"][1] - self.data["Regeneration"][0]) )
            self.resistance = self.data["Resistance"][0] + \
                int( self.niveau*abs(self.data["Resistance"][1] - self.data["Resistance"][0]) )
            self.energieMax = self.data["Energie"][0] + \
                int( self.niveau*abs(self.data["Energie"][1] - self.data["Energie"][0]) )
            self.vieMax = self.data["Vie"][0] + \
                int( self.niveau*abs(self.data["Vie"][1] - self.data["Vie"][0]))



        elif self.data["Apres"] != "":  
            self.__evolution()

    def _evolution(self) :
        self.__init__(self.data["Apres"])
    
    def refresh(self) :
        self.living = True
        self.vie = self.vieMax
        self.energie = self.energieMax


    def use_competence(self,other,n) :
        if self.energie >= self.competences[n].cout:
            print("{} utilise la competence {}".format(self.name,self.competences[n].name))
            self.competences[n].use(self,other)
            self.energie = max(0, self.energie - self.competences[n].cout)
            return True
        else:
            print("{} n'a pas assez d'energie".format(self.name))
            return False
        

    def __repr__(self) -> str:
        return "{} de niveau {} ({} xp) avec {} points de vie, {} energies (regeneration de {}) et une resistance de {}"\
        .format(self.data["Nom"], self.niveau, self.xp, self.vie, self.energie, self.regeneration, self.resistance)

        


class Competences(ABC) :
    def __init__(self,name,database) -> None:
        for c in database:
            if c["Nom"] == name : 
                self.data = c
                break
        if not hasattr(self, 'data'): raise ExistenceError
        self.name = name
        self.cout = self.data["Cout"]
        self.element = self.data["Element"]
        self.description = self.data["Element"]

    @abstractmethod
    def use(self):
        pass
    def __repr__(self) -> str:
        return self.name + ", "+ self.__class__.__name__+" de type " + self.element +", Cout :"+ str(self.cout) 



class Attaque(Competences):
    def __init__(self, name) -> None:
        super().__init__(name,attaque_database)

    def use(self,user:Pokemon,target:Pokemon):
        degat = 0
        if randint(0, 101 ) < self.data["Precision"]:
            success = True
            cm = TYPETAB[target.data["Element"]][self.data["Element"]] * uniform(0.85, 1)
            degat = round(  cm*( self.data["Puissance"]*(4*user.niveau + 2 )/target.resistance  )  + 2 )
            print("{} a effectué {} dégâts à {}".format(self.name,degat,target.name))

        else : 
            success = False
            print("{} a échoué".format(self.name))

        cost = self.data["Cout"]
        user.energie -= cost 
        target.vie -= degat

    def __repr__(self) -> str:
        return super().__repr__() + "\n\t Puissance : {}  Precision : {}".format(self.data["Puissance"],self.data["Precision"])

class Defense(Competences):
    def __init__(self, name) -> None:
        super().__init__(name,defense_database)

    def use(self,user:Pokemon,target:Pokemon):
        soin =  randrange(self.data["Soin"][0], self.data["Soin"][1] + 1 , 1)
        energie =  randrange(self.data["Energie"][0], self.data["Energie"][1] + 1, 1)
        cost = self.data["Cout"]
        
        user.vie += soin
        user.energie += energie
        user.energie -= cost 
        #return [True,cost,soin,energie ,0]
    def __repr__(self) -> str:
        return super().__repr__() + "\n\t Soin : {}  Energie : {}".format(self.data["Soin"],self.data["Energie"])

starters = [Pokemon("Bulbizarre"),Pokemon("Carapuce"),Pokemon("Salameche")]

if __name__ == "__main__":
    print(pokemon_database)

    starters[0].use_competence(starters[1],2)
