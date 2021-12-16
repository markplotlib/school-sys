import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

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

print('\nexample of date and time:')

# DATE(), TIME()
print(' basic date & time\n', cur.execute(
    'SELECT  DATE("now"), TIME("now")'
).fetchone())

print(' datetime (UTC default)\n', cur.execute(
    'SELECT  DATETIME("now")'
).fetchone())

print(' 2-week window\n', cur.execute(
    'SELECT  DATE("now", "-7 days"), DATE("now", "+7 days")'
).fetchone())

print(' +/- months\n', cur.execute(
    'SELECT  DATE("now", "-3 months"), DATE("now", "+3 months")'
).fetchone())

print(' UTC-08 (PST)\n', cur.execute(
    'SELECT  DATETIME("now", "-8 hours")'
).fetchone())

con.commit()
con.close()