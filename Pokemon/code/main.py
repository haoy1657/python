import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) ,"lib" ))
from lib import *
SAVES_DIR = os.path.join(os.path.dirname(__file__) ,"saves")
SAVES_DIR_DEFAULT = os.path.join(os.path.dirname(__file__) ,"saves","Default")


print("POOKemon 21-22 ® ")
print("by Abdelrahmaine,Mehdi & Malo ","\n")
jeu = True
saver = SaverDresseur(SAVES_DIR) 


while jeu:
    print("\n----------------------------------------")
    print("Choisissez le mode de jeu ")
    print("1) Exploration (JCE)")
    print("2) Mode Arene (JcJ)") 
    print("3) Quitter le Jeu")
    choix = input()
    if choix  == "1":
        mode = Exploration(saver)
    elif choix == "2" :  
        mode = Arene(saver)

    elif choix == "3" :  
        jeu = False
    else:
        print("Ce choix n'existe pas")