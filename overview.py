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

print('\nexample of COUNT DISTINCT:')
print('\n', cur.execute(
    'SELECT COUNT(*) FROM SUBJECTS'
).fetchone()[0], 'entries in Subjects table')

print('\n', cur.execute(
    'SELECT COUNT(GRADE) FROM SUBJECTS'
).fetchone()[0], 'are not null')

print('\n', cur.execute(
    'SELECT COUNT(DISTINCT GRADE) FROM SUBJECTS'
).fetchone()[0], 'are distinct (excluding null)')

print('\nexample of string functions:')

# REPLACE(col, x, y)
print('\n', cur.execute(
    '''
    SELECT  REPLACE(t.FIRST_NAME, 'Tomas', 'Tom')
            , REPLACE(t.LAST_NAME , 'Smith', 'Hanks')
    FROM        TEACHERS AS t
    WHERE       t.ID = 395
    '''
).fetchone())

# SUBSTR(col, start, stop)
print('\n', cur.execute(
    '''
    SELECT  SUBSTR(t.FIRST_NAME, 1, 4)
    FROM    TEACHERS AS t
    LIMIT 1
    '''
).fetchone()[0])

con.commit()
con.close()