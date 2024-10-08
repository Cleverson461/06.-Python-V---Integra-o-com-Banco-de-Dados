import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
""" 
    Cursor é um interador que permite navegar e manipular os registros em um BD
"""

cursor = connection.cursor()

# 3 - Lendo Dados da tabela
data = cursor.execute("""
    SELECT * FROM movies
                      """)
# SELECT * FROM movies
# SELECT name, year, score FROM movies
print(data.fetchall())
print()


# 4 - Iterando os Dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f'{row}')

print()
# 5 - Ordernando os Dados pelo Score
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f'{row}')
    
# 6 - Fechando a conexão
connection.close()