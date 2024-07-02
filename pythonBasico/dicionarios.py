<<<<<<< HEAD
               #Dicionarios
    #Criando Dicionarios
print("criando dicionarios")
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="GUilherme", idade=28)
print(pessoa)

pessoa ["telefone"] = "3333-1234"
print(pessoa)

print(40* "-")

    #acessar dados
print("#acessar dados")
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

    #Dicionario aninhado
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
print(contatos["giovana@gmail.com"]["nome"])

print(40* "-")
    #iterando dicionarios 
print("iterando dicionarios") 

for chave in contatos: 
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)
    
print(40* "-")

    #metodos
print("metodos")
print("CLEAR")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}

contatos.clear()
print(contatos)
print(40* "-")

    #COPY
print("COPY")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
copia = contatos.copy
print(copia)

    #fromkeys
print("fromkeys")
dict = dict.fromkeys(["nome", "telefone"])
print(dict)
dict = dict.fromkeys(["nome", "telefone"], "vazio")
print(dict)
print(40* "-")
    
    #get
print("get")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}
# contatos["chave"] #key error 

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))
print(40* "-")

    #items
print("items")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

print(contatos.items())
print(40* "-")
    #keys
print("keys")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}
print(contatos.keys())
print(40* "-")

    #Pop
#apaga com argumento
print("pop")
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "nao encontrou") #segundo argumento
print(resultado)
print(40* "-")

    #popitem
#apaga em ordem
print("popitem")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

print(contatos.popitem())
print(40* "-")

    #setdefault
print("setdefault")
contato = {'nome': 'Guilherme', 'telefone': '3333-0987'}

contato.setdefault('nome', 'giovana')
print(contato)

contato.setdefault("idade", 28)
print(contato)
print(40* "-")

    #Update
print("update")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

contatos.update({"guilherme@gmail.com": {"nome": "gui"}})
print(contatos)
print(40* "-")

    #values
print("values")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
print(contatos.values())
print(40* "-")

    #IN
print("In")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
resultado = "guilherme@gmail.com" in contatos
print(resultado)
resultado = "miguel@gmail.com" in contatos
print(resultado)
print(40* "-")

    #del
print("del")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}

del contatos["guilherme@gmail.com"]["telefone"]
print(contatos)
print(40* "-")
=======
               #Dicionarios
    #Criando Dicionarios
print("criando dicionarios")
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="GUilherme", idade=28)
print(pessoa)

pessoa ["telefone"] = "3333-1234"
print(pessoa)

print(40* "-")

    #acessar dados
print("#acessar dados")
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

    #Dicionario aninhado
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
print(contatos["giovana@gmail.com"]["nome"])

print(40* "-")
    #iterando dicionarios 
print("iterando dicionarios") 

for chave in contatos: 
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)
    
print(40* "-")

    #metodos
print("metodos")
print("CLEAR")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}

contatos.clear()
print(contatos)
print(40* "-")

    #COPY
print("COPY")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
copia = contatos.copy
print(copia)

    #fromkeys
print("fromkeys")
dict = dict.fromkeys(["nome", "telefone"])
print(dict)
dict = dict.fromkeys(["nome", "telefone"], "vazio")
print(dict)
print(40* "-")
    
    #get
print("get")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}
# contatos["chave"] #key error 

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))
print(40* "-")

    #items
print("items")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

print(contatos.items())
print(40* "-")
    #keys
print("keys")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}
print(contatos.keys())
print(40* "-")

    #Pop
#apaga com argumento
print("pop")
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "nao encontrou") #segundo argumento
print(resultado)
print(40* "-")

    #popitem
#apaga em ordem
print("popitem")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

print(contatos.popitem())
print(40* "-")

    #setdefault
print("setdefault")
contato = {'nome': 'Guilherme', 'telefone': '3333-0987'}

contato.setdefault('nome', 'giovana')
print(contato)

contato.setdefault("idade", 28)
print(contato)
print(40* "-")

    #Update
print("update")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
}

contatos.update({"guilherme@gmail.com": {"nome": "gui"}})
print(contatos)
print(40* "-")

    #values
print("values")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
print(contatos.values())
print(40* "-")

    #IN
print("In")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}
resultado = "guilherme@gmail.com" in contatos
print(resultado)
resultado = "miguel@gmail.com" in contatos
print(resultado)
print(40* "-")

    #del
print("del")

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "2134-8796"},
    "chappie@gmail.com": {"nome": "chappiee", "telefone": "1234-5678"},
    "melanie@gmail.com": {"nome": "melaine", "telefone": "5432-9870"},
}

del contatos["guilherme@gmail.com"]["telefone"]
print(contatos)
print(40* "-")
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
