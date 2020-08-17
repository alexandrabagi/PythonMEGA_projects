import psycopg2

# Process
# 1. Connect to the database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close connection

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    # establish connection with the database
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre1234' host='localhost' port='5432'")
    cur = conn.cursor()
    # insert data into the database
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

#insert_data("Water Glass",10,5)
#insert_data("Coffee Cup",16,9)

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(qantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgre1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (qantity, price, item))
    conn.commit()
    conn.close()

#create_table()
#insert_data("Orange", 15, 10)

#delete('Orange')
update(11,6,'Apple')
print(view())