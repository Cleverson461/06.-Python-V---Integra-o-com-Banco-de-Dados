import sqlite3 

# 1 - Criando BD
connection = sqlite3.connect("title.db")

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)