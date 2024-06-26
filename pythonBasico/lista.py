                #METODOS LISTAS
matriz = [    
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

                #FATIAMENTO
fatiamento = "FATIAMENTO"
print(fatiamento.center(20, "-"))

lista = ["F", "A", "T", "I", "A", "M", "E", "N", "T", "O"]

print(lista[2:])
print(lista[:2])
print(lista[:9:2])
print(lista[::])

                #LIST COMPREHRENSION
for item in lista:
    print(item)
for indice, item in enumerate(lista):
    print(f"{indice} º : {item}")
    
comp = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in comp if numero % 2 ==0]
impares = [numero for numero in comp if numero % 2 !=0]
print(f"numeros pares: {pares}")
print(f"numeros impares: {impares}")

quadrado = [numero ** 2 for numero in comp]
print(comp)
print(f" quadrado dos numeros: {quadrado}")


lista = [1, "Python", [40, 30 , 20]]

                #CLEAR
print(lista)
lista.clear()
print(lista)

                #COPY
lista = [1, "Python", [40, 30 , 20]]
lista.copy()
print(lista)    

                #COUNT
                
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

                #EXTEND
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])
print(linguagens)

            #INDEX
            
print(linguagens.index("java"))
print(linguagens.index("python"))

            #POP
            
linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

            #REMOVE
linguagens = ["python", "js", "c", "java", "ruby"]
linguagens.remove("java")
print(linguagens)

            #REVERSE

linguagens.reverse()
print(linguagens)

            #SORT
linguagens.sort()
linguagens.sort(reverse=True)
print(linguagens)
linguagens.sort(key=lambda x: len(x))
print(linguagens)

            #LEN

print(len(linguagens))

            #SORTED
            
sorted(linguagens, key=lambda x: len(x))
sorted(linguagens, key=lambda x: len(x), reverse=True)