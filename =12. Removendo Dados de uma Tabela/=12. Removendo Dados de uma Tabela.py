import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
""" 
    Cursor é um interador que permite navegar e manipular os registros em um BD
"""

cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja remover: "))

# 4 - Removendo Dados
cursor.execute("""
    DELETE FROM movies
    WHERE id = ?
                """, (id,))
connection.commit()
print("Filme removido com sucesso!")

# 5 - Fechando a conexão
connection.close()