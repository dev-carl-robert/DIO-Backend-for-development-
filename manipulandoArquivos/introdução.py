#Introdução
file = open(r"C:\Users\ROBERT\Desktop\teste.txt", "r")

for line in file.readlines():
    # print(line)
    pass

file.close()

#   Escrita

file1 = open("manipulandoArquivos/escrever.txt", "w")

file1.write("Sou muito lindo")
file1.writelines(["\n" "Pode acreditar","\n", "sem", "\n", "conversa"])
file1.close()