import sqlite3

with sqlite3.connect('bdd.db') as connexion:
    cursor = connexion.cursor()
    # script = "insert into coordonnees values(45.000003, 30.000000)"
    # cursor.execute(script)
    connexion.commit()
    script = "select * from coordonnees"
    cursor.execute(script)
    rows = cursor.fetchall()
    for row in rows:
        print(row)