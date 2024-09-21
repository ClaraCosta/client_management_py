import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


#------------------------- Criando uma nova tabela, novo banco, e inserindo registros-------------------------------------

conexao = sqlite3.connect(ROOT_PATH / "meubanco.db")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    #criacao de tabela co chaves primárias autoincrementadas
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))'
        )
    
def inserir_registro (conexao, cursor, nome, email):
    data = [nome, email]
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', data) #inserindo dados na table clientes
    conexao.commit() #é obrigatorio o uso do commit para os valores serem inseridos na tabela

def inserir_em_lote (conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (? ,?)', dados)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?', data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

''' 

Exemplo de tuplas para importação em lote

 dados = [
    ('Guilherme', 'email@guilherme.com'),
    ('João', 'email@joao.com'),
    ('Paulo', 'email@paulo.com'),
    ('Alice', 'email@alice.com'),
    ('Kassia', 'email@kassia.com'),
    ('Paloma', 'email@paloma.com'),
]'''

def consultar_um_registro (cursor, id):
    return cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    

def consultar_todos_registros (cursor):   
    return cursor.execute('SELECT * FROM clientes')



#cliente = consultar_um_registro(cursor, 6)
#print(dict(cliente))

#clientes = consultar_todos_registros(cursor)
#print(clientes)



