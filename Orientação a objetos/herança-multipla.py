<<<<<<< HEAD
class Animal():
    def __init__(self, nro_patas):
      self.nro_patas = nro_patas  
      
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
      self.cor_bico = cor_bico
      super().__init__(** kw)
    

class Cachorro(Mamifero): 
    pass
 
class Onitorrinco(Mamifero, Ave):
    pass

cachorro = Cachorro(nro_patas=4, cor_pelo="caramelo")
print(cachorro)

onitorrinco =Onitorrinco(nro_patas=2,cor_pelo= "vermelho", cor_bico= "laranja")
=======
class Animal():
    def __init__(self, nro_patas):
      self.nro_patas = nro_patas  
      
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
      self.cor_bico = cor_bico
      super().__init__(** kw)
    

class Cachorro(Mamifero): 
    pass
 
class Onitorrinco(Mamifero, Ave):
    pass

cachorro = Cachorro(nro_patas=4, cor_pelo="caramelo")
print(cachorro)

onitorrinco =Onitorrinco(nro_patas=2,cor_pelo= "vermelho", cor_bico= "laranja")
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(onitorrinco)