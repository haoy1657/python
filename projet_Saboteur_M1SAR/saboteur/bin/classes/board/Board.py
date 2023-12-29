"""
Created on Dec 23, 2022 12:31am 

@author: Viviane BAO, Hao Yuan
"""
import random
from classes.card.Card import *

class Board:

    def __init__(self):
        self.board = 0
        self.isComplete = False
        self.carte_arrivee = []
        self.start = []
        self.ligne, self.colonne = 7,8
        self.grid = self.fill_grid()

    def __str__(self):

        # Création du Board : 
        chaine = ""

        chaine += ' |' + ' '.join(['{:^5}'.format(j) for j in range(self.colonne)]) + "\n"
        chaine += '-+' + '-'.join(['-----' for j in range(self.colonne)]) + "\n"
    
        count = 0 
    
        for i in range(0, self.ligne * 3, 3):
        
            chaine += ' |' + ' '.join(['{}'.format(self.grid[i][j][2]) for j in range(self.colonne)]) + "\n"
            chaine += '{}|'.format(count) + ' '.join(['{:>5}'.format(self.grid[i+1][j][2]) for j in range(self.colonne)]) + "\n"
            chaine += ' |' + ' '.join(['{}'.format(self.grid[i+2][j][2]) for j in range(self.colonne)]) + "\n"
            count += 1
             
        chaine += '-+' + '-'.join(['-----' for j in range(self.colonne)]) + '-' + "\n"
        return chaine 
    
        
    def fill_grid(self):

        # Définition de la matrice grille en fonction de la taille souhaitée du board 
        # Création d'une grille de tuples de chaînes de caractères,la grille est composée de self.ligne * 3 lignes et self.colonne colonnes
        # Chaque tuple contient trois chaînes de caractères vides et un autre tuple qui contient une chaîne de caractères vide formatée avec '{:>5}'.format(''), 
        # Ce qui signifie que la chaîne sera alignée à droite sur une largeur de 5 caractères
        # Le double boucle for est utilisé pour créer une grille de tuples. La première boucle for itère sur les lignes de la grille 
        # Et la seconde boucle for itère sur les colonnes de chaque ligne

        # Définir la matrice grille en fonction de la taille souhaitee du board
        self.grid = [[("","",'{:>5}'.format('')) for i in range(self.colonne)] for j in range(self.ligne * 3)]

        # Dictionnaire des cartes arrivees
        self.carte_arrivee = {
            'carte_1': TreasureCard(True, True),
            'carte_2': TreasureCard(False, True),
            'carte_3': TreasureCard(False, True)
        }

        # Carte Depart : 
        start = StartCard(True)
        self.start = start.reveal_side
       
        # Melanger les cartes arrivees :

        items = list(self.carte_arrivee.items())
        random.shuffle(items)
        self.carte_arrivee = dict(items)

        
        # Position Start :
        l = int((self.ligne-1)/2)
        self.CardtoBoard(start.path,start.isPositive,self.start,l,0)
        
        # Position Carte arrivee 1 :
        self.CardtoBoard(self.carte_arrivee['carte_1'].path, self.carte_arrivee['carte_1'].isPositive, self.carte_arrivee['carte_1'].hide_side,0,self.colonne-1)
        
        # Position Carte arrivee 2 :
        self.CardtoBoard(self.carte_arrivee['carte_2'].path, self.carte_arrivee['carte_2'].isPositive, self.carte_arrivee['carte_2'].hide_side,l,self.colonne-1)
        
        # Position Carte arrivee 3 : 
        self.CardtoBoard(self.carte_arrivee['carte_3'].path, self.carte_arrivee['carte_3'].isPositive, self.carte_arrivee['carte_3'].hide_side,(self.ligne-1),self.colonne-1) 

        return self.grid   
        
    def CardtoBoard(self, card_type, isPositive, card, l, c):

    # La méthode commence par définir une variable pos comme étant égale à 3 * l. 
    # Cette valeur est utilisée pour déterminer les lignes de la grille où la carte doit être placée. 
    # Ensuite, la méthode itère sur une plage de valeurs allant de pos à pos + 3 (inclus)
    # Pour chaque valeur de cette plage, la méthode affecte un tuple à l'élément de la grille situé à la ligne row et à la colonne c. 
    #Le tuple contient les valeurs de card_type, isPositive et une chaîne de caractères de la carte (card[row%3]) 
    # En résumé, la méthode CardtoBoard prend en entrée une carte et des informations sur cette carte, puis place cette carte dans une grille à une position spécifique  
        pos = int(3 * l)
        for row in range(pos, pos + 3):
            self.grid[row][c] = (card_type, isPositive, card[row%3])

        return self.grid
           
   
    def check_complete(self,x,y):
    
    # on doit vérifier si le board est complet
    # on commence par définir une variable pos comme étant égale à 3 * x. 
    # Cette valeur est utilisée pour déterminer la ligne de la grille où se trouve la carte
    # "check_complete" vérifie si une carte dans la grille a des cartes voisines vides et, si c'est le cas, appelle une autre méthode sur l'objet self. 
    # Si la méthode appelée retourne True, l'attribut self.isComplete de l'objet est défini sur True, sinon l'attribut n'est pas modifié.

        pos = int(x * 3)

        left_card = [self.grid[pos][y-1][2],self.grid[pos+1][y-1][2],self.grid[pos+2][y-1][2]]
        right_card = [self.grid[pos][y+1][2],self.grid[pos+1][y+1][2],self.grid[pos+2][y+1][2]]
        top_card = [self.grid[pos-3][y][2],self.grid[pos-2][y][2],self.grid[pos-1][y][2]]
        bottom_card = [self.grid[pos+3][y][2],self.grid[pos+4][y][2],self.grid[pos+5][y][2]]
        


        if any(card == ['({:>3})'.format(''), '(END)', '({:>3})'.format('')]  for card in [left_card, right_card, top_card, bottom_card]):
            isGold = self.turn_carte_arrivee(x, y)
            if isGold : 
                self.isComplete = True
            else :
                return 
            
        return 
        
    
    def add_card(self, x, y, card):
    
    # On commence par définir une variable pos comme étant égale à 3 * x. 
    # Cette valeur est utilisée pour déterminer la ligne de la grille où la carte doit être placée
    # on utilise une boucle for pour vérifier si la carte peut être placée à la position souhaitée
    # Si l'un des éléments de la grille situés dans les lignes x à x+3 et dans la colonne y n'est pas une chaîne vide, la méthode retourne False sans continuer

        pos = int(x * 3)
        
        # On vérifie si la carte peut être placée à la position souhaitée
        for i in range(x, x + 3):
            if self.grid[i][y][2] != '{:>5}'.format(''):
                return False
       
        # Vérifier si les cartes adjacentes à la position souhaitée sont compatibles avec la carte que le joueur souhaite poser
        # Récupérer les cartes adjacentes

        # On récupère les types des cartes adjacentes à la position souhaitée
        left_card = [self.grid[pos][y-1],self.grid[pos + 1][y-1], self.grid[pos + 1][y-1] ]
        right_card = [self.grid[pos][y+1], self.grid[pos + 1][y+1], self.grid[pos + 1][y+1] ]
        top_card = [self.grid[pos-3][y], self.grid[pos-2][y], self.grid[pos-1][y] ]
        bottom_card = [self.grid[pos+3][y], self.grid[pos+4][y], self.grid[pos+5][y] ]

        # Vérifie si les cartes adjacentes à la position souhaitée sont compatibles avec la carte que le joueur souhaite poser

        if not self.are_compatible(left_card[0][0],left_card[0][1] ,card, "left", pos, y) and not self.are_compatible(right_card[0][0],right_card[0][1], card, "right", pos, y) \
          and not self.are_compatible(top_card[0][0],top_card[0][1], card, "top", pos, y) and not self.are_compatible(bottom_card[0][0],bottom_card[0][1], card, "bottom", pos, y):
            return False

        if all(card == '{:>5}'.format('') for card in [left_card[0][2], top_card[0][2], bottom_card[0][2]] ):
             return False

        # Si on arrive ici, c'est que la carte peut être placée à la position souhaitée    
        self.CardtoBoard(card.path, card.isPositive, card, x, y)
        # On vérifie si le Board est terminé
        self.check_complete(x,y)
        print(self.isComplete)

        return True

    def remove_card(self, x, y):
        
        vide = ['{:>5}'.format(''), '{:>5}'.format(''), '{:>5}'.format('')]
        
        # Ne peut pas enlever position carte arrivee et carte depart 
        removed_card = []
        pos = x*3

        for i in range(pos, pos+3, 1):
            removed_card.append(self.grid[i][y][2])
            
        # on vérifie si la carte à enlever est égale à la carte de départ ou à l'une des cartes d'arrivée (qui sont stockées dans un dictionnaire self.carte_arrivee) 
        #ou si la carte à enlever est vide (c'est-à-dire égale à la liste vide). Si l'une de ces conditions est vraie, la fonction renvoie False. 
        #Sinon, la fonction appelle la méthode CardtoBoard avec les arguments vides et les coordonnées x et y pour enlever la carte de la grille de jeu.
        if (removed_card == self.start) or (any(removed_card == value.hide_side for value in self.carte_arrivee.values())) or (removed_card == vide):
            print(self.carte_arrivee.values())
            return False
        else:
            self.CardtoBoard("","",vide,x,y)
        
        return True

    def are_compatible(self, adjacent_path, isPositive, card, position, pos, y):
     
        # On récupère le type de chemin de la carte adjacente à partir du tuple
        if isPositive:
            if position == "top":
                if card.path in ["U", "UR", "URDL", "URD", "UD"] and adjacent_path in ["D", "URDL", "URD", "UD"]:      
                    return True  
                else:
                    return False
            elif position == "right":
                if card.path in ["R", "UR", "URDL", "URL", "RL", "URD"] and adjacent_path in ["URDL", "UL", "RL", "URL"]:
                    return True
                else:
                    return False
            elif position == "bottom":
                if card.path in ["URDL", "URD", "UD", "URD", "URDL"] and adjacent_path in ["U", "UR", "UD", "URL", "URD", "URDL","UL"]:
                    return True
                else:
                    return False
            elif position == "left":
                if card.path in [ "URDL", "URL", "RL", "UL"] and adjacent_path in ["R", "UR", "URDL", "URL", "RL", "URD"]:
                    return True
                else:
                    return False
        else : 
            return False
    
    def turn_carte_arrivee(self, x, y):
        
        # Position correspondand à la carte arrivée 1 : 
        if (x == 0 and y + 1 == self.colonne - 1) or (x - 1 == 0 and y + 1 == self.colonne - 1):
            self.CardtoBoard(self.carte_arrivee['carte_1'].path, self.carte_arrivee['carte_1'].isPositive, self.carte_arrivee['carte_1'].reveal_side,0,self.colonne-1)
            # Renvoie True si en plus la carte retournée est une pépite pour mettre fin à la manche 
            if self.carte_arrivee['carte_1'].reveal_side == ['({:^3})'.format('|'),'({:^3})'.format('-G-'),'({:^3})'.format('|')] :
                return True

        # Position correspondand à la carte arrivée 2 :    
        elif (x == 3 and y + 1 == self.colonne - 1) or (x - 1 == 3 and y + 1 == self.colonne - 1 ) or (x + 1 == 3 and y + 1 == self.colonne - 1):
            self.CardtoBoard(self.carte_arrivee['carte_2'].path, self.carte_arrivee['carte_2'].isPositive, self.carte_arrivee['carte_2'].reveal_side, x ,self.colonne-1)
            if self.carte_arrivee['carte_2'].reveal_side == ['({:^3})'.format('|'),'({:^3})'.format('-G-'),'({:^3})'.format('|')] :
                return True
        # Position correspondand à la carte arrivée 3 :
        elif (x == 6 and y + 1 == self.colonne - 1) or (x + 1 == 6 and y + 1 == self.colonne - 1 ):
            self.CardtoBoard(self.carte_arrivee['carte_3'].path, self.carte_arrivee['carte_3'].isPositive, self.carte_arrivee['carte_3'].reveal_side,(self.ligne-1),self.colonne-1) 
            if self.carte_arrivee['carte_2'].reveal_side == ['({:^3})'.format('|'),'({:^3})'.format('-G-'),'({:^3})'.format('|')] :
                return True

        return False
