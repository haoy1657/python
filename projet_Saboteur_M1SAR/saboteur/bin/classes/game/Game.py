"""
Created on Dec 23, 2022 12:31am 

@author: Hao Yuan
"""

from classes.round.Round import Round
from classes.deck.Deck import Deck
from classes.player.Player import*
from classes.board.Board import Board


class Game:
    def __init__(self):
        self.actualRound = 0
        self.gold_cards= []
        self.rounds = 3
        self._nbPlayer = 0
        self.players = []

        
    @property
    def nbPlayer(self):
        return self._nbPlayer

    @nbPlayer.setter
    def nbPlayer(self, value):

        # Si l'utilisateur a entré un chiffre/nombre, on transforme la valeur en int 
        if value.isdigit():
            value = int(value)

        while (not(isinstance(value, int)) or not(3 <= value <= 10)):
        # Vérifie si les conditions du jeu sont respectées ou si un String non souhaité a été entré
            if  (value != "q") :
                value = input("Attention, le nombre de joueurs doit être un nombre entier compris entre 3 et 10 inclus. : ")
                if value.isdigit():
                    value = int(value)
            else : 
                return
    
        self._nbPlayer = value    

    def fill_players(self):
        """

        Remplit le tableau `players` avec des instances de la classe `Player`. 
        Demande à l'utilisateur de saisir le nom et l'âge de chaque joueur.
        Trie le tableau `players` dans l'ordre d'âge des participants (du plus jeune au plus âgé).

        """

        # Remplir le tableau players avec la classe Player
        for i in range(self.nbPlayer):
            nom = input(f'Entrez le nom du Joueur {i+1} : ')
            age = input(f"Entrez l'age du Joueur {i+1} : ")
   
            player = Player(nom)
            player.age = age

            self.players.append(player)
        
        # Trier le tableau players dans l'ordre d'âge des participants (du plus jeune au plus age)
        self.players.sort(key=lambda player: player._age)
        return self.players
              
    def startRound(self):

        """

        Cette fonction initialise une nouvelle manche de jeu. Elle crée un nouvel objet Board,
        remplit la pioche de cartes et mélange les cartes, puis attribue les rôles aux joueurs de manière aléatoire.
        Elle crée également un nouvel objet Round et initialise le tour du premier joueur. Enfin, la fonction
        exécute les tours de chaque joueur jusqu'à ce que la manche soit terminée, puis prépare la manche suivante (si nécessaire).
        """
        # Initialiser une nouvelle manche
        self.actualRound += 1

        board = Board() # ajouter les paramètres du Board
        self.deck= Deck()

        # Remplissage des pioches pour la manche courante :

        self.deck.fill_deck()
        self.deck.shuffle() 
        self.gold_cards = self.deck.gold_stack
        # Crée un objet Role afin d'attribuer les rôles aléatoirement par la suite : 
        roles = Role(self)

        # Remplis les mains de tous les joueurs et attribue les rôles : 
        for i in range(len(self.players)):
            self.players[i].getListCards(self.deck,self)
            self.players[i].getRole(roles)

        # Création de la Manche :
        self.current_round = Round(self, board, self.players[0], self.deck)
        self.current_player_index = 0

        # Faire jouer chaque joueur tour à tour jusqu'à la fin de la manche
        while not self.current_round.isEnded:
            print("Les joueurs sont les suivants : \n")
            for i in range (self.nbPlayer):
                print(f" Joueur {i+1} : {self.players[i].name}\n")

            print(f"\nC'est au tour du Joueur {(self.current_player_index % len(self.players))+1} : {self.current_round.actualDwarf.name} \n")
            self.current_round.turns()
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            self.current_round.actualDwarf = self.players[self.current_player_index]
        # Passage au Round suivant :

        self.setNextRound()
        return

    def setNextRound(self):

        """

        Prépare la prochaine manche d'un jeu.

        Distribue des cartes Or aux joueurs et met à jour la liste des joueurs en fonction de leur score. 
        Vérifie si la partie est terminée et, si ce n'est pas le cas, initialise une nouvelle manche.
        """

        # Distribuer les cartes Or aux joueurs 
        self.drawGold()
        
        # Mettre à jour la liste des joueurs en fonction de leur score
        self.players.sort(key=lambda value: value.gold)

        # Vérifier si la partie est terminée
        if self.endGame():
            return
        # Initialiser une nouvelle manche
        self.startRound()
        return

    def drawGold(self):
        """

        Distribue des cartes Or aux joueurs en fin de manche selon leur rôle et l'état du chemin.

        Si le chemin est ininterrompu, les Chercheurs d'or piochent une carte Or parmi celles disponibles et
        choisissent celle de valeur la plus élevée. Si le chemin n'est pas complet, les Saboteurs gagnent une
        certaine quantité de cartes Or en fonction de leur nombre.
    
        Ici on convertit directement dans player.gold la valeur de la Carte afin de calculer par 
        la suite plus facilement le score final. 
        """

        # Récupère le nombre de Saboteurs de la Manche
        nb_saboteurs = len([player for player in self.players if player.role == "Saboteur"])
        # Si le chemin est ininterrompu, c'est la fin de la manche et les Chercheurs d'or gagnent
        if self.current_round.board.isComplete():
             # On détermine le nombre de cartes Or à piocher
            nb_cards = self.nbPlayer if self.nbPlayer < 10 else 9

            # On pioche les cartes Or du jeu
            gold_cards = self.deck.gold_stack[:nb_cards]
            self.deck.gold_stack = self.deck.gold_stack[nb_cards:]

            # On répartit les cartes Or aux joueurs
            for player in self.players:
                if player.role == "Chercheur":
                    # Le joueur choisit une carte Or de la plus forte valeur possible
                    player.gold = max(gold_cards, key=lambda card: card.gold_count)
                    gold_cards.remove(player.gold_cards[-1])
        else :
        # Si le chemin n'est pas complet, les Saboteurs gagnent
            
            for player in self.players:
                if player.role == "Saboteur":
                   
                    if nb_saboteurs == 1:
                        player.gold += 4
                    elif nb_saboteurs in [2, 3]:
                        player.gold += 3
                    else:
                        player.gold += 2
        return
            
    def endGame(self):

        """

        Vérifie si la partie est terminée et détermine le gagnant si c'est le cas.

        La partie est considérée comme terminée lorsque toutes les manches ont été jouées. Le gagnant est
        alors déterminé en comparant le nombre de pépites d'or de chaque joueur.
        """

        # Vérifier si la partie est terminée (après toutes les manches)
        if self.actualRound == self.rounds:
            # Déterminer le gagnant = comparaison des nombres de pépite
            winner = self.players[0] 
            for player in self.players: 
                if player.gold > winner.gold:
                    winner = player
            print(f"Le gagnant est {winner.name} avec {winner.gold} pépites d'or!")
            return True
        return False        

class Sabooters():
    def __init__(self):
        self.game = None    

    def play(self):

        """
        Démarre une partie de Saboteur. Affiche un message de bienvenue et demande à l'utilisateur s'il souhaite démarrer une partie.
        Si l'utilisateur entre "non", la méthode `end` est appelée pour terminer le programme.
        Si l'utilisateur entre "oui", la méthode demande le nombre de joueurs et vérifie si c'est un nombre valide ou si l'utilisateur a 
        entré "q" pour quitter.
        Si c'est le cas, la méthode `end` est appelée.
        Sinon, un objet de la classe `Game` est créé et l'attribut `nbPlayer` de cet objet est mis à jour avec le nombre de joueurs entré par l'utilisateur.
        La méthode `fill_players` de l'objet `Game` est ensuite appelée pour remplir un tableau avec tous les objets `Player` de la partie, et la méthode `startRound` 
        est appelée pour démarrer la partie.
        """

        print("#"*100)
        print("#" + " "*98 + "#")
        print("#" + " "*33 + "Bienvenue dans le jeu Saboteur !" + " "*33 + "#")
        print("#" + " "*20 + "Préparez-vous à affronter vos amis dans ce défi stratégique." + " "*18 + "#")
        print("#" + " "*20 + "Suivez les instructions ci-dessous pour commencer à jouer. " + " "*19 + "#")
        print("#" + " "*98 + "#")
        print("#"*100)

        print("\n"*5)


        user_input = input("Voulez-vous commencer une partie ? (oui/non) : ")

        if user_input.lower() == "non":
            self.end()
        else : 

            user_input = input("Entrez le nombre de joueurs (entre 3 et 10 inclus) ou 'q' pour quitter: ")

            if user_input.lower() == 'q':
                self.end()
                return
           
            nb_players = user_input

            self.game = Game() 
            # Vérifie si on a entré un nombre de joueurs
            self.game.nbPlayer = nb_players 

            print("Le nombre de joueurs a été mis à jour avec succès.")
            print(f"Le nombre de joueurs est de {self.game._nbPlayer}.")

            # Remplis un tableau avec tous les objets Player de la partie : 
            self.game.fill_players()
            
            self.game.startRound()
        return

    def end(self):
        print("Merci d'avoir joué, au revoir !")
