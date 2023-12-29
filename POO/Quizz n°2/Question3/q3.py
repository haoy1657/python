class A : 
    def __init__ (self , a) : 
        self.a = a 
    
    def __eq__( self, other ) : 
        if not isinstance ( other , A ) :
            return False
            
        
        if( self is other ) :
            return True
        
            # 3/ On compare les champs d'interet
            # Egalite d'attribut
        
        if self.a != other.a :
            return False
        
        return True

a1 = A(-1) 
a2 = A(-1)
print(a1==a2) # Other == L'objet situé à droite  
print("-----------------")


class B(A) : 
    def __init__(self ,a , b) : 
        super().__init__( a ) 
        self.__b = b 
    
    @property
    def b(self) : return self.__b  # Lecture 
    
    
    
    def __eq__( self, other ) :
        if not isinstance ( other , B ) :
            return False
            
        
        if( self is other ) :
            return True
        
            # 3/ On compare les champs d'interet
            # Egalite d'attribut
        
        if self.b != other.b :
            return False
        
        return True


b1 = B(a1,-10) 
b2 = B(a1,-1)
print(b1==b2)