'''
1. connect to database
2. create a cursor object
3. query
4. execute
5. close
'''
import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

# insert("Potatoes",10,12.5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows         #returned as python list

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))    #only item so put ,
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity,price,item) )
    conn.commit()
    conn.close()

# delete('Potatoes')
# delete('Onion')
# delete('Tomato')
# insert('Onion',20,5.7)
# insert('Tomato',10,45)
print(view())
update(30,10,'Onion')
print(view())
