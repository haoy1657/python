"""
Created on Dec 23, 2022 12:31am 

@author: Hao Yuan
"""
from abc import ABC , abstractmethod

class Card(ABC):
    def __init__(self, type_card,isPositive):
        self._type_card = type_card
        self.isPositive = isPositive 

    def __len__(self):
        return 1

class ActionCard(Card):

    def __init__(self, type_action,isPositive):
        super().__init__("Action",isPositive)
        self.__type_action = type_action #
        self.__string = self.get_action_string()

    def __getitem__(self,index):
        return self.__string[index]  

    def get_action_string(self):

      
        self.__string = []
        
        if self.isPositive and self.__type_action != "MAP" and self.__type_action != "RoF" : 
            type = "DEF"
        elif not(self.isPositive) and self.__type_action != "MAP" and self.__type_action != "RoF" :
            type = "ATT"
        if self.__type_action=="MAP" :
            self.__string += ['({:^3})'.format('M'),'({:^3})'.format(self.__type_action),"({:^3})".format('P')]
        elif self.__type_action == "RoF":
            self.__string += ['({:^3})'.format('R'),'({:^3})'.format(self.__type_action),"({:^3})".format('F')]
        else: 
            if len(self.__type_action) == 2:
                self.__string += ['({:^3})'.format(type),'({:^3})'.format(self.__type_action),"({:>3})".format('')]
            else : 
                self.__string += ['({:^3})'.format(type),'({:^3})'.format(self.__type_action),"({:>3})".format('')]

        return self.__string
    
    def get_type_action(self):

    
        return self.__type_action

    def __str__(self):
       
        action_str = "\n".join(self.get_action_string())
        return action_str 
   

class GoldCard(Card):
    def __init__(self, gold_count):
        super().__init__("Or",True)
        self.__gold_count = gold_count #integer

  

class PathCard(Card):
    def __init__(self, type_path, isPositive):
        super().__init__("Path", isPositive)
        self.path_type = type_path

    @abstractmethod
    def get_path_string(self):
        pass

###################### Filles de PathCard ####################################

class TreasureCard(PathCard):
    def __init__(self, isGold, isPositive):
        super().__init__("Treasure", isPositive)
        self.path = "URDL"
        self.isGold = isGold
        self.reveal_side = self.get_revealSide(self.isGold)
        self.hide_side = self.get_hideSide()
    
    def __str__(self):
        return "\n".join(self.reveal_side)
    
    def get_path_string(self):
        return self.reveal_side
        
    def get_hideSide(self):

        # Code pour afficher le trésor sous forme de chaîne de caractères
        hide_side = ['({:>3})'.format(''), '(END)', '({:>3})'.format('')]
        return hide_side

    def get_revealSide(self,isGold):

  
        if isGold : 
            reveal_side = ['({:^3})'.format('|'),'({:^3})'.format('-G-'),'({:^3})'.format('|')]    
        else:
            reveal_side =['({:>3})'.format(''),'({:^3})'.format('R'),'({:>3})'.format('')]
        return reveal_side

class StartCard(PathCard):
    def __init__(self, isPositive):
        super().__init__("Start", isPositive)
        self.path = "URDL"
        self.reveal_side = self.get_path_string()

    def get_path_string(self):
        # Affiche la carte départ sous forme de chaîne de caractères
        path_str = ['({:^3})'.format('|'), '(-S-)', '({:^3})'.format('|')]
        return path_str
    
class SimplePathCard(PathCard):

    def __init__(self, path, isPositive):
        super().__init__("SimplePath", isPositive)
        self.path = path
        self.__string = self.get_path_string()

    def __getitem__(self,index):
        return self.__string[index]   

    def __str__(self): 
        path_str = "\n".join(self.get_path_string())
        return path_str

    def get_path_string(self):

        """
        
        Retourne une liste de chaînes de caractères représentant l'objet courant (une carte chemin) 
        sous forme de chaîne de caractères.
        La chaîne de caractères est obtenue en fonction du chemin indiqué par la carte (`path`) 
        et du type de carte (positive ou négative).
        """

        # Affiche la carte départ sous forme de chaîne de caractères
        self.__string = [] 

        if self.isPositive : 
            middle = "+"
        else :
            middle = "X"

        if self.path == "U":
            self.__string += ['({:^3})'.format('|'),'({:^3})'.format(middle),"({:>3})".format('')]
        elif self.path == "R":
            self.__string += ['({:>3})'.format(''),'({:>2}-)'.format(middle),"({:>3})".format('')]
        elif self.path == "UR":
            self.__string += ['({:^3})'.format('|'),'({:>2}-)'.format(middle),"({:>3})".format('')]
        elif self.path == "URDL":
            self.__string += ['({:^3})'.format('|'),'(-{:>1}-)'.format(middle),"({:^3})".format('|')]
        elif self.path == "URD":
            self.__string += ['({:^3})'.format('|'),'({:>2}-)'.format(middle),"({:^3})".format('|')]
        elif self.path == "URL":
            self.__string += ['({:^3})'.format('|'),'(-{:>1}-)'.format(middle),"({:>3})".format('')]
        elif self.path == "UL":
            self.__string += ['({:^3})'.format('|'),'(-{:<2})'.format(middle),"({:>3})".format('')]
        elif self.path == "UD":
            self.__string += ['({:^3})'.format('|'),'({:^3})'.format(middle),"({:^3})".format('|')]
        elif self.path == "RL":
            self.__string += ['({:^3})'.format(''),'(-{:^1}-)'.format(middle),"({:^3})".format('')] 

        return self.__string
   
#########################################################################################################



