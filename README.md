<h1>Client Management System</h1>

<p align=center><img height='100px' src='https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png'> 
<img height='100px' src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*fMPUMki182HzyVZvo_awDw.png'></p>

<br>
Este projeto é um sistema de gerenciamento de clientes que utiliza Python3 e SQLite3 para realizar operações de CRUD (Criar, Ler, Atualizar e Excluir) em uma base de dados local. Ele permite acessar, consultar e gerenciar registros de clientes de forma simples e eficiente.

<h3>Tecnologias utilizadas</h3>

- <img height='20px' src='https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png'> Python 3: Linguagem de programação principal utilizada no projeto.
- <img height='20px' src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*fMPUMki182HzyVZvo_awDw.png'> SQLite3: Banco de dados relacional utilizado para armazenar os dados dos clientes.
- Pipenv: Gerenciador de pacotes e ambiente virtual para dependências do Python.

<h3>Estrutura do projeto</h3>
A estrutura básica do projeto é a seguinte:

```shell
client_management_py/
│
├── .venv/                    # Ambiente virtual (não incluído no Git)
├── App/
│   ├── acessando_database.py  # Script para conexão e transações com o banco de dados
│   ├── consultando_clientes.py # Script para consultas de clientes
│   ├── transacao.py           # Script para realizar transações (inserção/exclusão)
│   ├── meubanco.db            # Banco de dados SQLite (local)
│
├── Pipfile                    # Lista de dependências do projeto
├── Pipfile.lock               # Lockfile do Pipenv (dependências bloqueadas)
├── pyproject.toml             # Arquivo de configuração do projeto
├── README.md                  # Documentação do projeto
├── .gitignore                 # Arquivo de configuração para ignorar arquivos no Git

```
<br>
<h3>Funcionalidades</h3>

- <b>Acessar banco de dados: </b> Conectar-se a um banco de dados SQLite3.
- <b>Consultar clientes:</b> Consultar registros de clientes armazenados no banco de dados.
- <b>Inserir e excluir clientes:</b> Permitir a adição e exclusão de registros de clientes.
- <b>Atualizar clientes individualmente e em lote:</b> Além da inserção de um só cliente, também permite a inserção de mais de um cliente ao mesmo tempo.

<h3>Requisitos</h3>

- Python 3.x
- SQLite3
- Pipenv para gerenciar o ambiente virtual

<h3>Instalação</h3>

1. Clone o repositório para a sua máquina local:
```shell
git clone https://github.com/seu-usuario/client-management-system.git
cd client-management-system
```

2. Crie um ambiente virtual e instale as dependências com Pipenv:
```shell
pipenv install
```

3. Ative o ambiente virtual:
```shell
pipenv shell
```
<br>
<h2>Como usar?</h2>

<b>Executando o programa:</b>

1. Para consultar clientes, execute o script de consulta:
```shell
python App/consultando_clientes.py
```

2. Para inserir ou excluir clientes
```shell
python App/transacao.py
```
<br>
<h3>Exemplo de uso</h3>

- <b>Consultar um cliente:</b> Ao executar o script de consulta, você será solicitado a inserir o ID do cliente. Se o cliente estiver no banco de dados, as informações serão exibidas, caso contrário, será solicitado um novo ID.

- <b>Excluir um cliente:</b>
Para excluir clientes, você pode usar o script transacao.py, passando os IDs dos clientes que deseja remover do banco de dados.

<br>
<br>
<br>

---
<h1>Licença</h1>
<b>Este projeto está licenciado sob a Licença MIT.</b>
<br><br>
<p><small>
MIT License

Copyright (c) 2024 Maria Clara Costa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</small>
</p>
---