# build a database specific to demo set operations
import sqlite3
import os

# filenames
dbfile = 'student-clubs.db'
sql_filename = 'student-clubs.sql'

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

# 3 disparate tables
print('demo: UNION')
z = cur.execute('''
          SELECT * FROM DRAMACLUB 
    UNION SELECT * FROM CHESSCLUB 
    UNION SELECT * FROM TRACKFIELD 
    ORDER BY FIRST_NAME ASC LIMIT 3''')
print(z.fetchall())
# result: it happens that one from each grade make the top 3 (one-in-six chance)

con.commit()
con.close()