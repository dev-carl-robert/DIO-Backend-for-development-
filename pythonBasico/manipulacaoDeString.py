curso = "python"

print(curso.upper())
print(curso.title())
print(curso.lower())
print(curso.center(10, "*"))
print("-".join(curso))
print(curso.split(" "))

print(f" estou estudando {curso.title()} pela DIO")

nome = "Carlos Robert Cabral Santos"

print(nome[0])
nomeSeparado = nome.split(" ")
print(nomeSeparado)
nomeDoMeio = nome[1]
print('.'.join(nome[::-1]))