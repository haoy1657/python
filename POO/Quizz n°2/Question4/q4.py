class Fonction:
    
    def __init__(self,a,b,x):
        
        self.__a=a ; self.__b=b ; self.__x=x
        
        
        
    def __str__(self):
        
        if not( self.__a <self.__x <self.__b ):
            
            return "Erreur : x doit être compris entre "+ str(self.__a)+" et "+ str(self.__b)
        else:
              return ( " Fonction({} , {} ,{})".format(self.__a , self.__b , self.__x) )
  

a, b=-7,6
x=20
newX=[-3,-2,6,-10,-6,6]

o=Fonction(a,b,x)
print(o)