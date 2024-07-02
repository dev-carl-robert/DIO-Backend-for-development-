<<<<<<< HEAD
# print(len("python"))
# lista = [10, 20, 30]
# print(len(lista))

class Passaro:
    def voar(self):
        print("voando....")
    
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()
        
        
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")
        
        
def plano_de_voo(obj):
    obj.voar()
plano_de_voo(Pardal())
=======
# print(len("python"))
# lista = [10, 20, 30]
# print(len(lista))

class Passaro:
    def voar(self):
        print("voando....")
    
    
class Pardal(Passaro):
    def voar(self):
        return super().voar()
        
        
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")
        
        
def plano_de_voo(obj):
    obj.voar()
plano_de_voo(Pardal())
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
plano_de_voo(Avestruz())