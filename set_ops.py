# build a database specific to demo set operations
import sqlite3
import os

# filenames
dbfile = 'set-ops.db'
sql_filename = 'honor-roll.sql'

if os.path.exists(dbfile): # overwrite only
    os.remove(dbfile)

con = sqlite3.connect(dbfile)
cur = con.cursor()

# DDL & insertions
sql_file = open(sql_filename)
sql_as_string = sql_file.read()

# takes about a half minute to build database
cur.executescript(sql_as_string)

# DB overview
q = '''
SELECT name FROM sqlite_schema
WHERE 
    type ='table' AND 
    name NOT LIKE 'sqlite_%';
'''
tables = cur.execute(q).fetchall()

print('Overview: table sizes\n', '-'*20)
for tbl in tables:
    print(tbl[0], end=': ')
    y = cur.execute('SELECT COUNT(*) FROM {}'.format(tbl[0]))
    print(y.fetchone()[0])



con.commit()
con.close()