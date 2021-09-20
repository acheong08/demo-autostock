import sqlite3
import socket
def startServer():
    global cmdStarter
    global s
    global c
    s = socket.socket()

    host = socket.gethostname()
    port = 12345
    s.bind((host,port))
    s.listen(0)

    c,addr = s.accept()

    print('Got connection from',addr)
    changeStock()

def changeStock():
    while True:
        change_amount = c.recv(1024).decode('utf-8')
        if int(change_amount) == 0:
            exit()
        modifyDB(change_amount)

def modifyDB(change_amount):
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    currentStock = cur.execute('SELECT stock FROM product WHERE name = ?',("Mint",)).fetchone()[0]
    newStock = currentStock + int(change_amount)
    cur.execute("UPDATE product SET stock = ? WHERE name = ?", (newStock, "Mint",))
    print("Stock: " + str(cur.execute('SELECT stock FROM product WHERE name = ?',("Mint",)).fetchone()[0]))
    conn.commit()
    conn.close()
while True:
    startServer()
