# print("""
#     IO Error: erro de entrada e saida
#         erro de permissão
#         falta de espaço
#     """)

# print("""
#     UnicodeDecode Error: erro de decodificação
#         decodificação inadequada
#     """)

# print("""
#     UnicodeDecode Error: erro de codificação
#         codificação inadequada
#     """)

# print("""
#       Is a directory error: 
#       quando se abre o diretorio em vez do arquivo txt 
#       """
#       )
from pathlib import Path

try:
    arquivo = open("meuArquivo.py")
except FileNotFoundError:
    print("arquivo não encontrado")
    

ROOT_PATH = Path(__file__).parent
try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except Exception:
    print("não foi possivel abrir o arquivo")