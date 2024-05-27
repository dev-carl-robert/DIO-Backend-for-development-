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
plano_de_voo(Avestruz())