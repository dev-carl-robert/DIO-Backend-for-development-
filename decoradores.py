def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos!"

def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")

print(mensagem_para_guilherme(dizer_oi))
print(mensagem_para_guilherme(incentivar_aprender))

def pai():
    print("escrevendo da pai() função")
    
    def filho1():
        print("escrevendo da filho1() função")
    
    def filho2():
        print("escrevendo da filho1() função")
    filho1()    
    filho2()
    
pai()    
    
print(40* "_")

def calcular(operacao):
    def somar(a, b):
        return a + b
    def subtrair(a, b):
        return a - b
    
    if operacao == "+":
        return somar
    else:
        return subtrair

resultado = calcular("+")(1, 3)
print(resultado)


print(40* "_")
def mensagem(nome):
    print('executando nome')
    return f"Oi {nome}"

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f"Olá tudo bem com você {nome}"

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

print(executar(mensagem, "joao"))
print(executar(mensagem_longa, "joao"))

print(40* "_")

print("função interna")

def principal():
    print("executando a função principal")
    def funcao_interna():
        print("executando a funcao interna")
        
    def funcao2():
        print("executando a funcao 2")
    
    funcao_interna()
    funcao2()

principal()


print(40* "_")

print("retorna função")

def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a,b):
        return a - b
    
    def mul(a, b):
        return a + b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        
op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("+")
print(op(2, 2))

print(40* "_")
print("decorador")

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope
    
def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

print(40* "_")
print("Açúcar Sintático")

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo")
    
ola_mundo()