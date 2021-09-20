import sqlite3

connection = sqlite3.connect('product.db')


with open('product.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO product (name, stock) VALUES (?, ?)",
            ('Mint', 10)
            )
connection.commit()
connection.close()
