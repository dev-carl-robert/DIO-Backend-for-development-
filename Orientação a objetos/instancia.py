<<<<<<< HEAD
class Estudantes:
    escola = "DIO"
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"

def mostrar__valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudantes("Guilherme", 1)
aluno_2 = Estudantes("Giovanna", 2)

=======
class Estudantes:
    escola = "DIO"
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"

def mostrar__valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudantes("Guilherme", 1)
aluno_2 = Estudantes("Giovanna", 2)

>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
mostrar__valores(aluno_1, aluno_2)