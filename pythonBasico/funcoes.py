<<<<<<< HEAD
        #FUNÇÕES
print("criando funções")
def exibir_mensagem():
    print("olá mundo!")
def exibir_mensagem_2(nome):
    print(f"Seja Bem vindo {nome}")
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja Bem vindo {nome}")
exibir_mensagem()
exibir_mensagem_2(nome="GUilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="CHappie")
print(40* "-")

        #retornando valores
print("retornando valores")
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor
print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(40* "-")

        #ARGUMENTO NOMEADOS
print("argumentos nomeados")
def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
print(40* "-")

=======
        #FUNÇÕES
print("criando funções")
def exibir_mensagem():
    print("olá mundo!")
def exibir_mensagem_2(nome):
    print(f"Seja Bem vindo {nome}")
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja Bem vindo {nome}")
exibir_mensagem()
exibir_mensagem_2(nome="GUilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="CHappie")
print(40* "-")

        #retornando valores
print("retornando valores")
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor
print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(40* "-")

        #ARGUMENTO NOMEADOS
print("argumentos nomeados")
def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
print(40* "-")

>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
