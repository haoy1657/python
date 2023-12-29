"""
Created on Dec 23, 2022 12:31am 

@author: Hao Yuan
"""

from classes.card.Card import *
import random

class Deck:
    
    def __init__(self):
        self.game_stack = []
        self.gold_stack = []

    def __str__(self):
        result = f"La pioche contient {len(self.game_stack)} cartes :\n"
        for card in self.game_stack:
            result += f"\n{card}\n"
        return result
  

    def fill_deck(self):

        """

        Remplit deux paquets de cartes : `game_stack` et `gold_stack`.
        Le paquet `game_stack` contient des cartes chemin et des cartes action. Pour chaque type de carte, la méthode ajoute une certaine quantité de cartes positives et négatives.
        Le paquet `gold_stack` contient des cartes or de différentes valeurs.
        """

        # Remplir le paquet de jeu avec les cartes chemin

        for path, nb_positive, nb_negative in [("URDL", 5, 1), ("URD", 5, 1), ("URL", 5, 1), ("UR", 5, 1), ("UL", 4, 1), ("UD", 4, 1), ("RL", 3, 1), ("U", 0, 1), ("R", 0, 1)]:
            
            self.game_stack.extend([SimplePathCard(path, True) for i in range(nb_positive)])
            self.game_stack.extend([SimplePathCard(path, False) for i in range(nb_negative)])

       # Remplir le paquet de jeu avec les cartes action
        for action_type, nb_positive, nb_negative in [("L", 2, 3), ("P", 2, 3), ("W", 2, 3), ("LP", 1, 0), ("LW", 1, 0), ("PW", 1, 0), ("MAP", 6, 0), ("RoF", 3, 0)]:
            
            self.game_stack.extend([ActionCard(action_type, True) for i in range(nb_positive)])
            self.game_stack.extend([ActionCard(action_type, False) for i in range(nb_negative)])

       # Remplir le paquet d'or avec les cartes or
        for gold_value, nb_cards in [(1, 16), (2, 8), (3, 4)]:
            self.gold_stack.extend([GoldCard(gold_value) for i in range(nb_cards)])
            
        return self.game_stack, self.gold_stack 
    
    def shuffle(self):
        
        """

        Mélange les paquets de cartes. 
        """
        random.shuffle(self.game_stack)
        random.shuffle(self.gold_stack)
    
    
    

  



