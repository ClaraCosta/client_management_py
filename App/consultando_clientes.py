import sqlite3
from pathlib import Path

#------------------Conexão com o banco-------------------

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meubanco.db")
cursor = conexao.cursor()




#----------------------Aplicação-----------------------

def solicita_id_cliente(conexao, cursor, id):
    while True:
        
        id_cliente = input('Informe o id do cliente: ')
        cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
        cliente = cursor.fetchone()
        

        if id_cliente.upper() == 'Q':
            print("------------------------------------------------------")
            print("O programa será encerrado, seu registro foi encontrado.")
            print("------------------------------------------------------")
            break

        if cliente is None:
            print("Esse registro não foi localizado, tente novamente.")
        else:
            print("------------------------------------------------------")
            print(f"Cliente encontrado: {cliente}")
            print("O programa será encerrado, seu registro foi encontrado.")
            print("------------------------------------------------------")
            break
        


print("------------- Consulta de clientes--------------------")
print(" Pressione [Q] para finalizar o programa")
print("------------------------------------------------------")
solicita_id_cliente(conexao, cursor, id)

