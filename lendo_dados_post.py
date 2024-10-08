from conexo_post import conn

curso_obj = conn.cursor()

curso_obj.execute("SELECT * FROM game")

result = curso_obj.fetchall()

print(result)
