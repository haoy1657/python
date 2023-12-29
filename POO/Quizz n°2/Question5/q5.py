import numpy as np

class A :
    def __init__(self,a):
        self.a=a
    def m1(self):
        return self
        """ Return aléatoire , pour pouvoir faire l'addition plus bas """
        
class B (A):
    def __init__(self,a,b):
        #super().__init__(self,a)
        self.a=a
        self.b=b
    def m1(self):
        return self
        
class C (A):
    def __init__(self,a,c):
         #super().__init__(self,a)
        self.a=a
        self.c=c
    def m1(self):
        return self
    
class Tab :
    

    """ Pour choix : 0 == classe A , 1 == classe B , 2 == classe C """
    """Pour l'élement de la classe considérée , on prend l'objet situé au meme index que celui du choix de la classe """
    """ ex : 0 en index 5 == 5 e objet de la classe A """

    def __init__(self,t):
        self.t=t
        
    def __str__(self):
     
        nbA=self.t.count(0)  # On compte le nombre d'objet de la classe A dans le tableau choix 
        
        nbB=self.t.count(1) #  On compte le nombre d'objet de la classe B dans le tableau choix 
        
        nbC=self.t.count(2) #  On compte le nombre d'objet de la classe C dans le tableau choix 
    
        
        m1a,m1b,m1c=0,0,0 #  Somme des elements de la classe A , B ou C 
        for i in range (len(self.t)): # Parcours de t (Choix)
    
            if self.t[i]==0 : # Objet de la classe A 
                m1a += A.m1(self.t[i]) # appel de la méthode m1 de la classe A pour cette valeur de t[i] (Somme)
            if self.t[i]==1 :
                m1b+=B.m1(self.t[i])
            if self.t[i]==2 :
                m1c+=C.m1(self.t[i])

        res="A : {},{} \n".format(nbA,m1a)
        res+="B : {},{}\n ".format(nbB,m1b)
        res+="C : {},{} ".format(nbC,m1c)
        return res                              
    


choix=[2,1,1,0]
vA=[-3,-5,0,3]
vB=[-1,3,5,6]
vC=[7,8,1,4]

a=A(vA)
b=B(vA,vB)
c=C(vA,vC)
tab=Tab(choix)

print(tab)


""" A partir de choix on choisis va , vb ou vc """
""" Choix est dans le programme principal """