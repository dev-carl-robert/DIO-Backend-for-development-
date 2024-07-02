<<<<<<< HEAD
# Iteradores

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
                
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros = [38, 13, 11]):
    print(i)
    
=======
# Iteradores

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
                
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros = [38, 13, 11]):
    print(i)
    
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
