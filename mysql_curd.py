import mysql.connector

# mysql config
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="curd_database"
)

# print(mydb)

mycursor = mydb.cursor()

# Show database
'''
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)
'''

# Create Table using below command
'''
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255) )")
mycursor.execute("CREATE TABLE cus (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255) )")
'''

# Add column into table
'''
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
'''

# Check if a table exist 
'''
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''


# insert singal value data into table
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ('john', 'Highway 21')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
'''

# insert multiple data value data into table
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
'''


# insert single value and get lastrowid
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ('john', 'Highway 21')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.lastrowid, ":  Lastrowid")
'''


# retrive all data using following code
'''
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''

# retrive one data using following code
'''
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
for x in myresult:
    print(x)
'''

# select with a filter
'''
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# Prevent SQL Injection
'''
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
'''


# Sort the result
'''
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# Delete Record
'''
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Records deleted")
'''

# Delete a Table
'''
sql = "DROP TABLE customers"
mycursor.execute(sql)
'''


# Delete the table "customers" if it exists
'''
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql) 
'''


# update tables
'''
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected") 
'''

# Limit the Result (Start from position 3, and return 5 records)
'''
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
'''

# Join Two or More Tables
'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
'''

# LEFT JOIN
'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
'''

# RIGHT JOIN
'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x) 
'''
