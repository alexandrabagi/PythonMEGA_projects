import sqlite3

# Process
# 1. Connect to the database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close connection

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    # establish connection with the database
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # insert data into the database
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()

#insert_data("Water Glass",10,5)
#insert_data("Coffee Cup",16,9)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(qantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (qantity, price, item))
    conn.commit()
    conn.close()

#delete('Wine Glass')
update(11,6,'Water Glass')
print(view())