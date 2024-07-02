import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# os.mkdir(ROOT_PATH / "novo-diretorio")

# arquivo = open(ROOT_PATH / "novo.txt", "w")
# os.remove(ROOT_PATH / "novo.txt")


shutil.move(ROOT_PATH / "escrever.txt", ROOT_PATH / "novo-diretorio" / "escrever.txt")