import sqlite3
from pathlib import Path

#------------------Conexão com o banco-------------------

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meubanco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 1', 'teste1@gmail.ccom'))
    conexao.commit()
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?)', ('3','Teste 1', 'teste1@gmail.ccom'))
    conexao.commit()

except Exception as exc:
    print(f'Ops! um erro ocorreu! {exc}')
    conexao.rollback()

