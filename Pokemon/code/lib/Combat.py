import Personnage
from Pokemon import *
class Combat:
    def __init__(self, joueur1, joueur2):
        self.J1 : Personnage = joueur1
        self.J2 : Personnage = joueur2
        self.J1.combat = True 
        self.J2.combat = True 
        self.tour = 1
        self.combat = True
        self.winner = None
        self.J1.refresh()
        self.J2.refresh()
        print("\n--------------------------------------------------------------------")
        print("\nLe combat qui oppose {} a {} commencé\n".format(self.J1.name,self.J2.name))
        
        while self.combat:
            self.jouer_tour()
            self.tour += 1
        print("Le Joueur n°{} alias {} remporte le combat au tour {}".format(self.winner[0], self.winner[1].name, self.tour ))

    def jouer_tour(self):
        print("------------------------------------------------------------")
        print("Tour",self.tour)
        print("Joueur n°1 {} a {} points de vie".format(self.J1.pokemonActif.name,self.J1.pokemonActif.vie))
        print("Joueur n°2 {} a {} points de vie".format(self.J2.pokemonActif.name,self.J2.pokemonActif.vie))



        print("\nJoueur n°1 {} à toi ".format(self.J1.name))
        self.J1.jouer_tour(self.J2)
        if self.__check_combat() : return 
        print("\nJoueur n°2 {} à toi ".format(self.J2.name))
        self.J2.jouer_tour(self.J1)
        if self.__check_combat() : return 
        self.tour += 1
        self.J1.pokemonActif.energie += self.J1.pokemonActif.regeneration
        self.J2.pokemonActif.energie += self.J2.pokemonActif.regeneration


    def __check_combat(self):
        if self.J1.combat == False :
            self.winner = [2,self.J2]
            self.combat = False  
            return True 
        if self.J2.combat == False :
            self.winner = [1,self.J1]
            self.combat = False
            return True




if __name__ == "__main__":        
    S1= Personnage.Dresseur("Sacha",starters)
    S2= Personnage.PokemonSauvage("Pikachu")

    print(starters)
    Combat(S1,S2)