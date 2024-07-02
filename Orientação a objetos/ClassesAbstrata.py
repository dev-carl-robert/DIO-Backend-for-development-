<<<<<<< HEAD
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    
    def marca(self):
        pass
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("ligando a tv")
        print("ligada")
        
    def desligar(self):
        print('Desligando a tv..')
        print("desligada")
    
    @property
    def marca(self):
        return "LG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o ar condicionado")
        print("ligada")
    
    def desligar(self):
        print('Desligando o ar condicionado..')
        print("desligado")
    
    @property
    def marca(self):
        return "LG"
   

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
=======
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    
    def marca(self):
        pass
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("ligando a tv")
        print("ligada")
        
    def desligar(self):
        print('Desligando a tv..')
        print("desligada")
    
    @property
    def marca(self):
        return "LG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o ar condicionado")
        print("ligada")
    
    def desligar(self):
        print('Desligando o ar condicionado..')
        print("desligado")
    
    @property
    def marca(self):
        return "LG"
   

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(controle.marca)