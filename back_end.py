import sqlite3

# 5 steps for sqlite

# connect to db
# create a cursor
# apply sql query
# commit changes
# close the connection
    
class Database(object):
    
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, shelf TEXT, price TEXT, quantity TEXT, section TEXT)")
        self.con.commit()
        
    def insert(self, title="", author="", shelf="", price=0, quantity=0, section=""):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?,?)", (title, author, shelf, price, quantity, section))
        self.con.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows
    
    def search(self, title="", author="", shelf="", price=0, quantity=0, section=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR shelf=? OR price=? OR quantity=? OR section=?", (title, author, shelf, price, quantity, section))
        rows = self.cur.fetchall()
        return rows
    
    def delete(self, ids):
        self.cur.execute("DELETE FROM book WHERE id = ?", (ids,))
        self.con.commit()
        
    def update(self, id, title, author, shelf, price, quantity, section):
        self.cur.execute("UPDATE book SET title=?, author=?, shelf=?, price=?, quantity=?, section=? WHERE id=?", (title, author, shelf, price, quantity, section, id))
        self.con.commit()      
        
    def __del__():
        self.con.close()