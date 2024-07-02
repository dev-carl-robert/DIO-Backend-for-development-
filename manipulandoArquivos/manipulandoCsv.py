import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "escrever.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(['1', "maria"])
        escritor.writerow(["2", "joao"])
except IOError as exc:
    print(f"erro ao criar o arquivo : {exc}")

try:
    with open(ROOT_PATH / "escrever.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"erro ao criar o arquivo : {exc}")

