from conexo_post import conn

cursor_obj = conn.cursor()

games = [
    ('Start Wars Survisor', 2023, 9.0),
    ('Luigis Mansion 3', 2019, 9.0)
]

for game in games:
    cursor_obj.execute("""
        INSERT into game(name, year, score)
        VALUES (%s, %s, %s)
                       """, game)
    
conn.commit()
print("Dados inseridos com sucesso.")
conn.close()