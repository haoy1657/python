# -*- coding: utf-8 -*-


class Matrice : 
    def __init__ (self , coeff) : 
        self.coeff = coeff 
    
    def __str__(self): 
             
        res  = ""
        for k in self.coeff:
            res += "| " + " | ".join([str(i) for i in k ]) + " |\n"
        
        return res

M = Matrice( [["3","2","1"],["4","6","4"]])
print(M)


""" The strip() method returns a copy of the string by removing both 
the leading and the trailing characters (based on the string argument passed)."""

""" USE str.replace() TO REMOVE A COMMA FROM A STRING IN PYTHON """

