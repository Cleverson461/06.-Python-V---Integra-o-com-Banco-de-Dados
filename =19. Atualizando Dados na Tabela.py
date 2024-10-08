from conexo_post import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE game
    SET name = %s, year = %s, score = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ("Fifa 01", 2021, 7.5, 5))
    
conn.commit()
print("Dados atualizados com sucesso.")
conn.close()