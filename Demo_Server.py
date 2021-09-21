#Import modules (SQL and networking)
import sqlite3
import socket
import os
#This function listens on port 12345 for connections
def startServer():
    #Set variables to be global (Allows for interaction in any function)
    global s
    global c
    #Define socket (interface for networking)
    s = socket.socket()
    #Get local IP address. Can change to 0.0.0.0 if allow remote connections
    host = socket.gethostname()
    #Set port number
    port = 12345
    #Bind and listen on port
    s.bind((host,port))
    s.listen(0)
    #Accept connections and notify on connect
    c,addr = s.accept()
    print('Got connection from',addr)
    #Run the stock controller when connected
    changeStock()

def changeStock():
    #Keep running while true until 0 is entered
    while True:
        #Get number from network connection
        change_amount = c.recv(1024).decode('utf-8')
        if int(change_amount) == 0:
            #Asks for reason for exit
            c.sendall("Enter reason for exit: ".encode('utf-8'))
            log_reason_for_exit = str(c.recv(1024).decode('utf-8'))
            #Save reasoning to exit.log (RCE here)
            command = str("echo '" + log_reason_for_exit + "' >> exit.log")
            os.system(command)
            exit()
        #Pipe the number into the function modifyDB
        modifyDB(change_amount)

def modifyDB(change_amount):
    #Connect to SQL database
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    #Get current number of stocks available
    currentStock = cur.execute('SELECT stock FROM product WHERE name = ?',("Mint",)).fetchone()[0]
    #Add value from changeStock() to current number of stock available
    newStock = currentStock + int(change_amount)
    #Update database with new stock number
    cur.execute("UPDATE product SET stock = ? WHERE name = ?", (newStock, "Mint",))
    #Outputs new stock number
    print("Stock: " + str(cur.execute('SELECT stock FROM product WHERE name = ?',("Mint",)).fetchone()[0]))
    #Commit changes and close database connection
    conn.commit()
    conn.close()
#Start server
while True:
    startServer()
