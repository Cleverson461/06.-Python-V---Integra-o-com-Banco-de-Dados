import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
""" 
    Cursor é um interador que permite navegar e manipular os registros em um BD
"""

cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input("Informe o id do filme que deseja atualizar: "))
name = input("Informe o novo nome do filme: ")
year = int(input("Ano do Filme: "))
score = float(input("Nota do Filme: "))


# 4 - Atualizando Dados
cursor.execute("""
    UPDATE movies 
    SET name = ?, year = ?, score = ?
    WHERE id = ?
               """, (name, year, score, id))
connection.commit()
print("Dados Atualizados com sucesso!")

# 5 - Fechando a conexão
connection.close()