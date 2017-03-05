import sqlite3

# 5 steps for sqlite

# connect to db
# create a cursor
# apply sql query
# commit changes
# close the connection

def create_table():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, shelf TEXT, price REAL, quantity INTEGER, section TEXT)")
    con.commit()
    con.close()
    
def insert(title, author, shelf, price, quantity, section):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?,?)", (title, author, shelf, price, quantity, section))
    con.commit()
    con.close()
    
def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="", author="", shelf="", price=0, quantity=0, section=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR shelf=? OR price=? OR quantity=? OR section=?", (title, author, shelf, price, quantity, section))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(ids):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (ids,))
    con.commit()
    con.close()
    
def update(id, title, author, shelf, price, quantity, section):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, shelf=?, price=?, quantity=?, section=? WHERE id=?", (title, author, shelf, price, quantity, section, id))
    con.commit()
    con.close()