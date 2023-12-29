"""
Created on Dec 23, 2022 12:31am 

@author: Hao Yuan
"""
import random
from classes.card.Card import *

class Player:

    def __init__(self, name):
        self.name = name
        self._age = 0
        self.gold = 0
        self.hand = []
        self.role = None
        self.tools= {
            
            'L': "right", # Lampe
            'W': "right", # Wagon
            'P': "right"  # Pick
        }

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        # Si l'utilisateur a entré un chiffre/nombre, on transforme la valeur en int 
        if value.isdigit():
            value = int(value)

        while not(isinstance(value, int)):

            value = input("Attention, l'âge doit être un nombre entier : " )
            # Si l'utilisateur a entré un chiffre/nombre, on transforme la valeur en int 
            if value.isdigit():
                value = int(value)

        self._age = value
        

    def getListCards(self, deck, _Game):

        """
        Remplit la main du joueur courant (`self.hand`) avec des cartes piochées 
        dans le paquet de jeu (`deck.game_stack`).
        Le nombre de cartes piochées dépend du nombre de joueurs dans la partie (_Game._nbPlayer).
        """
        # Remplis la main du joueur en fonction du nombre de joueurs dans la Partie 

        if 3 <= _Game._nbPlayer <= 5:
            [self.hand.append(deck.game_stack.pop()) for i in range(6)]
        elif 6 <= _Game._nbPlayer <= 7:
            [self.hand.append(deck.game_stack.pop()) for i in range(5)]
        elif 8 <= _Game._nbPlayer <= 10:
            [self.hand.append(deck.game_stack.pop()) for i in range(4)]
        return self.hand

    def drawCard(self, deck):

        """

        Fait piocher une carte au joueur courant dans le paquet de jeu (`deck.game_stack`).
        La carte piochée est ajoutée à la main du joueur courant.
        """
        # Fait piocher une carte au joueur dans le paquet de jeu et met à jour sa main et le deck
        self.hand.append(deck.game_stack.pop())
        return self.hand   

    def getRole(self,_Roles):
        """

        Donne un rôle au joueur courant parmi les rôles restants dans la liste des rôles (_Roles.roles).
        Le rôle est retiré de la liste des rôles (_Roles.roles) et est affecté au joueur courant.
        """
        self.role = _Roles.roles.pop()
        return self.role

    def showRole(self):
        """

        Affiche le rôle du joueur courant.
        """
        return f"Vous êtes : {self.role}"

    def showHand(self):

        """

        Affiche la main du joueur courant sous forme de chaîne de caractères.
        La chaîne de caractères contient les cartes de la main du joueur ainsi que l'option 
        de défausser une carte.
        """
        hand_string = ""

        # Parcourt chaque colonne du tableau "cards"
        for i in range(len(self.hand[0])*3):
            # Parcourt chaque vecteur dans le tableau "cards"
            for card in self.hand:
                # Ajoute chaque colonne du vecteur à la chaîne de caractères
                if isinstance(card, SimplePathCard):

                    hand_string += card.get_path_string()[i] + "   "
                else:
                    hand_string += card.get_action_string()[i] + "   "
            hand_string += "\n"  # Ajoute un retour à la ligne à la fin de chaque colonne

        # Ajoute les numéros en dessous des cartes à la chaîne de caractères
        for i, card in enumerate(self.hand):
            # Utilisez la fonction "format" pour centrer le numéro sous la carte
            hand_string += "{:^5}".format(i+1) + "   "

        # Ajoute l'indice 7 à la chaîne de caractères
        hand_string += "\n\n7   Défausser une carte \n\n"

        return hand_string
    
    def showArrivedCard(self):
        string = "\n"
        card = ['({:>3})'.format(''), '(END)', '({:>3})'.format('')]
        cards = [card] * 3
        for i in range (len(cards)):
            for j in range(3):
                print(cards[i][j])
            print("{:^5}".format(i+1) + "\n")
        string += "\n"
        return string


    def play_action(self, round_board, round, action):

        """
        Permet à un joueur de jouer une action en fonction de son choix et du type de carte qu'il a choisi. 
        Si la carte est une carte "MAP" ou "RoF", l'action correspondante sera effectuée. Si la carte est une carte "L", "P", "W", "LP", "LW" ou "PW", 
        l'action sera effectuée sur le joueur ciblé en fonction de si la carte est positive ou négative. Si l'action est réalisée avec succès, 
        la carte est supprimée de la main du joueur.
        """
        card = self.hand[action-1]
        # Récupérer le type d'action de la carte
        action_type = card.get_type_action()

        # Traiter la carte selon son type d'action
        if action_type == "MAP":
            
            print(self.showArrivedCard())
            indice = input(" Quelle carte arrivée souhaitez-vous voir (entre 1 et 3 inclus) ? :")

            print("La voici : \n")
            print(round_board.carte_arrivee[f'carte_{indice}'], "\n")
            self.hand.pop(action-1)  
            return True
       
        elif action_type == "RoF":
            
            
            print("Quelle carte voulez-vous supprimer ? : ")

            x = int(input(f"Entrez la coordonnée x (entre 0 et {round_board.ligne - 1} inclus) : "))
            y = int(input(f"Entrez la coordonnée y (entre 0 et {round_board.colonne - 1} inclus) : "))

           
            # On tente de placer la carte sur le plateau de jeu
            if not round_board.remove_card(x, y):
            # Si la carte ne peut pas être placée, on redemande au joueur de sélectionner de nouvelles coordonnées
                print("Impossible de retirer cette carte / Cet emplacement est déjà vide. \n")
                return False
               
            else : 
                print("La carte chemin a bien été retirée !")
                self.hand.pop(action-1) 
                return True 

        elif action_type in ["L", "P", "W", "LP", "LW", "PW"] :
            
            target = int(input("Quel joueur veux-tu viser avec cette carte ? (Choisir le numéro du joueur : 1, 2, ...) : "))
            target = round.game.players[target-1]

            if action_type in ["LP", "LW", "PW"]:
                new_action = input(f"Vous avez utilisé la carte {action_type}. \n Sur quel outil voulez-vous l'utiliser ? (L/P/W) : ")
                action_type = new_action

            # Si on veut casser un outil : 
            if not card.isPositive : 
    
                if target != self:

                    print(action_type)
                    target.tools[action_type] = "break"
                    print(f"L'outil {action_type} de {target.name} a été cassé.")
                    self.hand.pop(action-1)
                    return True

                else :
                    print("Vous ne pouvez pas casser vos propres objets ... ! ")
                    input("Appuyez sur Entrée pour continuer...")
                    return False

            # Si on veut réparer un outil :
            else : 

                if not(self.tool_condition(target, action_type, card)):
                    target.tools[action_type] = "right"   
                    if target != self:
                        print(f" L'outil {action_type} de {target.name} a été réparé.")
                        self.hand.pop(action-1)  
                        return True
                    else :
                        print(f" Votre outil {action_type} a été réparé.")
                        self.hand.pop(action-1)  
                        return True

                else :    
              
                    print("La carte que vous voulez utiliser ne peux pas être utilisé sur ce joueur.")
                    input("Appuyez sur Entrée pour continuer... \n")
                    return False

    def place_card(self, round_board, action):

        """
        Demande au joueur de sélectionner les coordonnées x et y où il souhaite poser une carte. 
        La méthode appelle ensuite la méthode add_card de l'objet round_board en lui passant les coordonnées x, y,
        et la carte qui se trouve à l'indice action-1 dans la main du joueur. 
        Si la carte a pu être placée, elle est retirée de la main du joueur et la méthode retourne 
        True, sinon elle affiche un message d'erreur et retourne False.
        """
        
        # On demande au joueur de sélectionner les coordonnées de la carte à poser
        print("Vous souhaitez placer une Carte Chemin : \n")
        x = int(input(f"Entrez la coordonnée x (entre 0 et {round_board.ligne - 1} inclus) : "))
        y = int(input(f"Entrez la coordonnée y (entre 0 et {round_board.colonne - 1} inclus) : "))
       
        
        
        # On tente de placer la carte sur le plateau de jeu
        
        if  round_board.add_card(x, y, self.hand[action-1]) :
        # Si la carte a pu être placée, on la retire de la main du joueur
            self.hand.pop(action-1)
                
            return True

        else:
            # Si la carte ne peut pas être placée, on redemande au joueur de sélectionner de nouvelles coordonnées
            print("\nImpossible de poser la carte à cet emplacement. \n")
            return False
       
         

    def discard_card(self):
        """
        Demande au joueur de sélectionner une carte à défausser et la retire de sa main. 
        Retourne la liste des cartes restantes dans la main du joueur.
        """
        indice = int(input("Quelle carte voulez-vous défausser ? : "))
        self.hand.pop(indice-1)
        return self.hand

    def tool_condition(self, target, tool, card):

        """
        Vérifie d'abord l'état de l'outil spécifié par l'entier tool de l'objet target. 
        Si l'outil est cassé ("break"), la méthode vérifie si la carte est positive et retourne True dans ce cas, 
        sinon elle retourne False. Si l'outil n'est pas cassé, la méthode vérifie si la carte est négative et 
        retourne True dans ce cas, sinon elle retourne False.
        """
        if target.tools[tool] == "break":
            # Si l'outil est cassé, la carte doit être positive pour être jouée
            if card.isPositive:
                return True
            else:
                return False
        else:
            # Si l'outil n'est pas cassé, la carte doit être négative pour être jouée
            if card.isPositive:
                return False
            else:
                return True

#################################################################

class Role:

    def __init__(self, _Game):
        self.game = _Game
        self.roles = self.fill_roles()

    def fill_roles(self):

        """        
        Crée une liste roles vide et définit le nombre de joueurs de type "Mineur" et de type "Saboteur" en fonction 
        du nombre total de joueurs stocké dans l'attribut nbPlayer de l'objet game. La liste roles est remplie avec les rôles 
        qui ont été définis et mélangée aléatoirement à l'aide de la fonction random.shuffle. 
        """
        roles = []

        # Définir le nombre de Saboteurs et de Mineurs en fonction du nombre de joueurs :

        if self.game.nbPlayer == 3:
            for role_type, nb_role in [("Mineur", 3), ("Saboteur", 1)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 4:
            for role_type, nb_role in [("Mineur", 4), ("Saboteur", 1)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 5:
            for role_type, nb_role in [("Mineur", 4), ("Saboteur", 2)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 6:
            for role_type, nb_role in [("Mineur", 5), ("Saboteur", 2)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 7:
            for role_type, nb_role in [("Mineur", 5), ("Saboteur", 3)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 8:
            for role_type, nb_role in [("Mineur", 6), ("Saboteur", 3)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 9:
            for role_type, nb_role in [("Mineur", 7), ("Saboteur", 3)]:
                roles.extend([role_type for i in range(nb_role)])
        elif self.game.nbPlayer == 10:
            for role_type, nb_role in [("Mineur", 7), ("Saboteur", 4)]:
                roles.extend([role_type for i in range(nb_role)]) 

        random.shuffle(roles)

        return roles          
