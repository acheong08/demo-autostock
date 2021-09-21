# demo-autostock
By: Antonio Cheong

# What is this?
This is an example of how a stock keeping software would work. It is only meant as a demo and therefore lacks any complex features. The only available stock item
is Mint. `Demo_Server.py` listens on port `12345`. When connected to the server, any number entered is used to modify the stock of Mint. Enter `5` and the stock will
increase by `5`. Can subtract by entering negative number.
# I messed up the database... What should I do?
Run `Demo_SQL.py` to reset the database. The default stock volume is 10.
# Working on:
- Authentication
- Example security vulnerabilities
- Client side

## **Usage**
Download project:
`git clone https://github.com/acheong08/demo-autostock`
`cd demo-autostock`
`pip3 install sqlite3 socket` (Modules might be pre-installed)
Start server:
`python3 Demo_Server.py`
On another terminal:
`nc localhost 12345 -v`
Whithin the nc command, enter integers only.
