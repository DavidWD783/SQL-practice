import sqlite3
from sqlite3 import Error

con = sqlite3.connect("DatabaseName.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Contacts (Fname TEXT,
Lname TEXT, Phone INTEGER)""")

Fname = input("Enter first name: ")
Lname = input("Enter last name: ")
Phone = input("Enter telephone number(no dashes or spaces): ")
Phone = int(Phone)


cur.execute("""INSERT INTO Contacts (Fname, Lname, Phone)
VALUES (?,?,?)""", (Fname,Lname,Phone))

con.commit()

cur.close()
con.close()