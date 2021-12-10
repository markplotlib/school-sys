# build a database (create Connection object representing database)
import sqlite3
import os

dbfile = 'school-sys.db'

con = sqlite3.connect(dbfile)

# create a cursor object
cur = con.cursor()

# DDL
ddl = '''CREATE TABLE ppl (
    ID INT PRIMARY KEY,
    FIRST_NAME TEXT,
    LAST_NAME TEXT
);'''

cur.execute(ddl)

# DML
dml = "INSERT INTO ppl VALUES(101,'Jo','Jo')"
cur.execute(dml)

# query
qry = "SELECT * FROM ppl"
y = cur.execute(qry)
print(y.fetchall())

con.commit()
con.close()