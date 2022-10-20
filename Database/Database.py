import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE players ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")