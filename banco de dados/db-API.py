import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect("cliente.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?, ?);", data) 
    conexao.commit()
    
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()
    
def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()
    
def inserindo_em_lote(conexao, cursor, data):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', data)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    # print(cliente)
    pass

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))