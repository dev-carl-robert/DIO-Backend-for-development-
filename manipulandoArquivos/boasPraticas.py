from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(ROOT_PATH / 'escrever.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError:
    print("erro ao abrir o arquivo")