<<<<<<< HEAD
        #FUNÇÃO SET
print("função set:")
numeros = ([1, 2, 3, 1, 3, 4, 2])
print(set(numeros))

carros = ("palio", "gol", "celta", "celta")
print(set(carros))

        #FATIAMENTO
print("função set:")
numeros = {1, 2, 3, 1, 3, 4, 2}
numeros = list(numeros)

print(numeros[2])

        #ITERAR CONJUNTOS
print("ITERAR CONJUNTOS:")
carros = {"palio", "gol", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

        #UNION
print("UNION:")
conjunto_a = {1, 2}
conjunto_b = {3, 4}

        #INTERSECTION
print("INTERSECTION:")

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.intersection(conjunto_b))

        #DIFFERENCE
print("DIFFERENCE:")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
        #symmetric difference
print("symmetric difference:")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.symmetric_difference(conjunto_a))

        #issubset
print("issubset: ")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
        
        #issuperset
print("issuperset: ")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

        #isdisjoint
print("isdisjoint: ")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

        #sorteio
        
sorteio = {1, 23}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(22)
print(sorteio)
sorteio.add(27)
=======
        #FUNÇÃO SET
print("função set:")
numeros = ([1, 2, 3, 1, 3, 4, 2])
print(set(numeros))

carros = ("palio", "gol", "celta", "celta")
print(set(carros))

        #FATIAMENTO
print("função set:")
numeros = {1, 2, 3, 1, 3, 4, 2}
numeros = list(numeros)

print(numeros[2])

        #ITERAR CONJUNTOS
print("ITERAR CONJUNTOS:")
carros = {"palio", "gol", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

        #UNION
print("UNION:")
conjunto_a = {1, 2}
conjunto_b = {3, 4}

        #INTERSECTION
print("INTERSECTION:")

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.intersection(conjunto_b))

        #DIFFERENCE
print("DIFFERENCE:")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
        #symmetric difference
print("symmetric difference:")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.symmetric_difference(conjunto_a))

        #issubset
print("issubset: ")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 5, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
        
        #issuperset
print("issuperset: ")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

        #isdisjoint
print("isdisjoint: ")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

        #sorteio
        
sorteio = {1, 23}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(22)
print(sorteio)
sorteio.add(27)
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(sorteio)