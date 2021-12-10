import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

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