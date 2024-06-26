class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print("ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self, status):
        self.status = status
        if status == True:
            print("carregado")
        else: 
            print("não estou carregado")

moto = Motocicleta('preta', 'abc1234', 2)
moto.ligar_motor()

carro = Carro('azul', "abe293", 4)
caminhao = Caminhao('vermelho', "ab42d3", 8, True)

print(moto)
print(caminhao)
print(carro)