<<<<<<< HEAD
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
      
    @classmethod    
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        if idade >= 18:
            return "é maior de idade"
        else:
            return "é menor de idade"     

p = Pessoa.criar_apartir_data_nascimento(ano=2002, mes=3, dia=21, nome="guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(23))
=======
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
      
    @classmethod    
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        if idade >= 18:
            return "é maior de idade"
        else:
            return "é menor de idade"     

p = Pessoa.criar_apartir_data_nascimento(ano=2002, mes=3, dia=21, nome="guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(23))
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(Pessoa.e_maior_idade(8))