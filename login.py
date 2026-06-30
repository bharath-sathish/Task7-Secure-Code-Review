import sqlite3

username = input("Enter Username: ")
password = input("Enter Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

cursor.execute(query)

print("Login Successful")
