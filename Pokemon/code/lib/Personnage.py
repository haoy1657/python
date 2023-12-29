import random
from typing import List
from Pokemon import * 

class Personnage(ABC):
    def __init__(self,name) -> None:
        self.name = name
        self.combat = False

    @property
    @abstractmethod
    def pokemonActif() -> Pokemon:
        pass

    @property
    @abstractmethod
    def combat():
        pass

    @abstractmethod
    def jouer_tour():
        pass

    @abstractmethod
    def refresh():
        pass

    def __repr__(self) -> str:
        return self.name

class Dresseur(Personnage):

    def __init__(self,name,start_pokemons: List[Pokemon] = starters) -> None:
        super().__init__(name)
        self.pokemons = start_pokemons
        self.deck = [self.pokemons.pop(0) for _ in range(min(3,len(self.pokemons)))]

            


    @property
    def pokemonActif(self) -> Pokemon :
        if self.deck[0].living == False:
            print("{} n'est plus en état de combattre {} le remplace".format(self.deck[0].name,self.deck[1].name))
            self.deck = self.deck[1:] + self.deck[0]
        return self.deck[0]

    @property
    def combat(self):
        if [pokemon.living == True for pokemon in self.deck] != [True] * len(self.deck):
            self.combat = False
        return self._combat
    @combat.setter
    def combat(self,value):
            self._combat = value
    
    def refresh(self):
        for pokemon in self.deck:
            pokemon.refresh()
    
    def jouer_tour(self,other):
        print("1) Utiliser une competence")
        print("2) Envoyer un autre Pokemon")
        print("3) Fuir ")
        if other.__class__.__name__ == "PokemonSauvage" and other.pokemonActif.vie <= 0.2 * other.pokemonActif.vieMax :
            print("4) Capturer le Pokemon ")

        while True:
            choix = input()
            # Utiliser une competence
            if choix == "1":
                print("{} a {} points d'énergie".format(self.pokemonActif.name,self.pokemonActif.energie))
                if self.choisir_competences(other.pokemonActif) == False:
                    # Si utilisation de competence annule rejouer le tour 
                    self.jouer_tour(other.pokemonActif)
                break
            # Envoyer un autre Pokemon
            elif choix == "2":
                if self.choisir_PokemonActif() == False:
                    # Si choisir_PokemonActif annule rejouer le tour 
                    self.jouer_tour(other.pokemonActif)
                break
            # Fuir
            elif choix == "3":
                print("{} a fuit".format(self.name))
                self.combat = False
                break
            # Si c'est un Pokemon sauvage tenter de le capturer
            elif choix == "4" and other.__class__.__name__ == "PokemonSauvage" and other.pokemonActif.vie <= 0.2 * other.pokemonActif.vieMax :
                if random.random() < 4*(0.2 - other.pokemonActif.vie/other.pokemonActif.vieMax):
                    print("La capture de {} a reussi ".format(other.pokemonActif.name))
                    self.capture(other.pokemonActif)
                    other.pokemonActif.vie = 0
                else:
                    print("La capture de {} a échouée ".format(other.pokemonActif.name))
                break

            else:
                print("Ce choix n'existe pas")
                continue
    
    def choisir_deck(self):
        self.pokemons = self.pokemons + self.deck
        self.deck = []
        choix_tab = []
        for i,p in enumerate(self.pokemons):
            print("{}) {}".format(i+1,p))
        k = min(len(self.pokemons), 3)
        for i in range(k):
            while True:
                choix = input("Choisissez votre Pokemon n°{} ".format(i + 1))
                if not choix.isdigit : 
                    print("Concentrez vous ce n'est pas un entier !!!")
                    continue
                else : choix = int(choix) - 1
                if choix > len(self.pokemons) : 
                    print("Malheureusement vous n'avez pas autant de pokemons. Continuer d'en capturer !!!") 
                    continue
                elif choix in choix_tab:
                    print("Vous avez deja choisit ce pokemon.")
                else:
                    choix_tab.append(choix)
                    break
        self.deck = [self.pokemons[i] for i in choix_tab]
        [self.pokemons.pop(i) for i in sorted(choix_tab,reverse=True)]


    
    def choisir_competences(self,other):
        print("Choisir quelle competence utiliser")
        for i,c in enumerate(self.pokemonActif.competences):
            print("{}) {}".format(i+1,c))
        print("{}) Annuler".format(len(self.pokemonActif.competences)+1))

        while True:
            choix = input()
            if not choix.isdigit : 
                print("Concentrez vous ce n'est pas un entier !!!")
                continue
            else : choix = int(choix) - 1

            if choix > len(self.pokemonActif.competences) + 1: 
                print("Ce Pokemon n'a pas autant de competence") 
                continue
            else:
                if choix == len( self.pokemonActif.competences )  :
                    return False
                self.pokemonActif.use_competence(other,choix)
                return True

    def choisir_PokemonActif(self):
        # Affiche les pokemons possede
        for i,pokemon in enumerate(self.deck):
            print("{}) {}".format(i+1,pokemon))
        print("{}) Annuler".format(len(self.deck)+1))
        while True:
            choix = input()
            if not choix.isdigit : 
                print("Concentrez vous, vous n'avez pas saisie un nombre entier !!!")
                continue
            else : choix = int(choix) 
            if choix == len(self.deck ) +1 :
                return False
            if choix > len(self.deck) : 
                print("votre deck ne contient que {} pokemons".format(len(self.deck))) 
                continue
            else:
                self.deck.insert(0,self.deck.pop(choix-1)) 
                print(self.deck)
                break
        return True 
        

    def capture(self,pokemon):
        self.pokemons.append(pokemon)

    def __repr__(self) -> str:
        return super().__repr__() + str(self.deck)



class PokemonSauvage(Personnage):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._pokemonActif : Pokemon = Pokemon(name)

    @property
    def pokemonActif(self):
        return self._pokemonActif

    @property
    def combat(self):
        if self.pokemonActif.living == False:
            self.combat = False
        return self._combat
    @combat.setter
    def combat(self,value):
            self._combat = value


    def refresh(self):
        self.pokemonActif.refresh()
    def jouer_tour(self,other):
        other = other.pokemonActif
        self.pokemonActif.use_competence(other,randint(0,len(self.pokemonActif.competences) - 1))
        


if __name__ == "__main__":        
    p = Dresseur('toto',[Pokemon("Carapuce"),Pokemon("Carapuce"),Pokemon("Carapuce"),Pokemon("Carapuce"),Pokemon("Carapuce"),])
    p != None
    p.choisir_deck()
    print(p.deck)
    print(p.pokemons)


