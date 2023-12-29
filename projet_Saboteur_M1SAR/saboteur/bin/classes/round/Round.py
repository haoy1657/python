"""
Created on Dec 23, 2022 12:31am 

@author: Hao Yuan
"""

from classes.deck.Deck import Deck
from classes.player.Player import Player
from classes.card.Card import*


class Round:
    def __init__(self,_Game, _Board,_Player,_Deck):
        self.board = _Board
        self.isEnded = False
        self.actualDwarf = _Player
        self.deck = _Deck
        self.game = _Game
        

    def turns(self):

        """

        Effectue un tour de jeu pour le joueur en cours dans une partie. 
        Demande à l'utilisateur quelle carte il souhaite utiliser et vérifie si elle peut être jouée sur le plateau de jeu.
        Si le paquet de jeu n'est pas vide, le joueur pioche une carte, sinon, non.
        La méthode vérifie si la manche est terminée également.
        """

        print(self.board)
        print(self.actualDwarf.showRole(), "\n")
        print(f"Etat des outils : L = {self.actualDwarf.tools['L']} , W = {self.actualDwarf.tools['W']} et P = {self.actualDwarf.tools['P']} \n")
        print(f"\nPioche : {len(self.deck.game_stack)} carte(s)\n")
        print(self.actualDwarf.showHand())

         # Exécuter les actions du joueur en cours
        while True:

            action = input(f"Quelle carte voulez vous utiliser (1 à {len(self.actualDwarf.hand)})? : ")
            if action.isdigit():
                action = int(action)
        
            while not(isinstance(action, int)) or not( 1 <= action <= len(self.actualDwarf.hand) + 1 )  :
                action = input("Entrez une valeur valide : ")
                if action.isdigit():
                    action = int(action)
                continue
        
            # On vérifie d'abord si le joueur souhaite défausser une carte : 
            if action == len(self.actualDwarf.hand) + 1 :
                self.actualDwarf.discard_card()
                break

            elif isinstance(self.actualDwarf.hand[action-1], ActionCard):
                if self.actualDwarf.play_action(self.board, self, action):
                    break
                else : 
                    continue

            elif isinstance(self.actualDwarf.hand[action-1], PathCard):
                all_tools_intact = True
            # On teste d'abord si le joueur peut poser une carte sur le Board : 

                for tool, status in self.actualDwarf.tools.items():
                    if status == "break":
                        all_tools_intact = False
                        break

                if all_tools_intact:
                    if self.actualDwarf.place_card(self.board, action):
                        break
                    else :
                        continue
                else : 
                    print("Vous devez réparer vos outils avant de pouvoir poser une carte. ")
                    continue

        # Réinitialise le Board après l'action du joueur actuel 
               
        print(self.board)

        if len(self.deck.game_stack) != 0:
            self.actualDwarf.drawCard(self.deck) # Fait piocher une carte au joueur dans le paquet de jeu et met à jour sa main et le deck
        
        input("Appuyez sur Entrée pour laisser la main au joueur suivant : ")    
        print("\n" * 50)
        input("Joueur suivant : appuyez sur Entrée dès que vous êtes prêt : ")
        print("\n" * 10)

        # Mettre à jour l'état du tour
        self.check_end()
         

    def check_end(self):

        """
        
        Vérifie si la manche est terminée.
        La manche se termine si la gallerie est complète ou si tous les joueurs ont épuisé leurs cartes en main.
        """


        # La manche se termine également lorsque la gallerie est complete
        if self.board.isComplete:
            self.isEnded = True
            return     

        # La manche se termine lorsque tous les joueurs ont epuise leurs cartes en main
        for player in self.game.players:
            if len(player.hand) > 0:
                return       
        self.isEnded = True
       
        

