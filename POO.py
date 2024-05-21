class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha
    def buzinar(self):
        print("plim plim")      
    def parar(self):
        print("parando....")
    def correr(self):    
        print("vrummmm..")
    def trocar_marcha(self, nro_marcha):
        print("trocando marcha..")
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("marcha trocada")
            else:
                print("não foi possivel")    

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bicicleta("vermelha", "caloi", 2022, 600, 1)
print(b1)
# Bicicleta.buzinar(b1)
# Bicicleta.correr(b1)
# Bicicleta.parar(b1)
# print(b1.cor, b1.modelo, b1.ano, b1.valor)


