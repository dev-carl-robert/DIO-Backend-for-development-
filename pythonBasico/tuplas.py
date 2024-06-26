        # usando construtor tuple
print(40 * "_")
print("usando o construtor tuple: ")
letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

print(40 * "_")
print("virgula no final = tupla ")
pais = ("Brasil",) #virgula no final = tupla
print(pais)

        #acesso direto
print(40 * "_")
print("acesso direto ")
frutas = ("maçã", "uva", "mamão",)
print(frutas)
print(frutas[-1])
print(frutas[2])

        #Tuplas aninhadas
print(40 * "_")
print("Tuplas aninhadas ")
matriz = (
    (1, "a", 2),
    ("b", 4, 2),
    ("p", "o", 2),
)

print(matriz[0])
print(matriz[0][2])
print(matriz[0][-1])

        #fatiamento
print(40 * "_")
print("fatiamento ")
letras = tuple("python")

print(letras)
print(letras[2:])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::2])
