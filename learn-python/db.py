import mysql.connector as conn

mydb = conn.connect(
  host="localhost",
  user="root",
  passwd="rgukt123",
  database="test_database"
)

# print(mydb) 

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE test_database")

# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)

# cursor.execute("CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), email VARCHAR(100), password VARCHAR(150), phone VARCHAR(20))")

# query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"

# values = ('Hari', 'hari@gmail.com', '8309092927')

# cursor.execute(query, values)

# mydb.commit()

# print(cursor.rowcount, "record inserted.")






