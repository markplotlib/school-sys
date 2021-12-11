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

# UNION
z = cur.execute('''
          SELECT LAST_NAME, GRADE FROM DRAMACLUB 
    UNION SELECT LAST_NAME, GRADE FROM CHESSCLUB 
    UNION SELECT LAST_NAME, GRADE FROM HIKECLUB 
    ORDER BY LAST_NAME ASC LIMIT 3''')
print(z.fetchall())

# INTERSECT
a = cur.execute('''
          SELECT FIRST_NAME FROM DRAMACLUB
    INTERSECT SELECT FIRST_NAME FROM CHESSCLUB''')
drama_chess = a.fetchall()
print('\nIn drama and chess clubs:', drama_chess[0][0], ',', drama_chess[1][0])

b = cur.execute('''
          SELECT FIRST_NAME FROM DRAMACLUB
    INTERSECT SELECT FIRST_NAME FROM CHESSCLUB
    INTERSECT SELECT FIRST_NAME FROM HIKECLUB
    ''')
drama_chess_hike = b.fetchall()
print('In all 3 clubs:', drama_chess_hike[0][0])


# set differences
e = cur.execute('''
    SELECT FIRST_NAME FROM DRAMACLUB
    EXCEPT
    SELECT FIRST_NAME FROM CHESSCLUB
    ''')
drama_not_chess = e.fetchall()
print('in drama but not in chess:', drama_not_chess)

f = cur.execute('''
    SELECT FIRST_NAME FROM CHESSCLUB
    EXCEPT
    SELECT FIRST_NAME FROM DRAMACLUB
    ''')
chess_not_drama = f.fetchall()
print('in chess but not in drama:', chess_not_drama)


# UNION ALL vs UNION
cte = '''WITH all_clubs AS (
            SELECT FIRST_NAME FROM CHESSCLUB
            UNION {} SELECT FIRST_NAME FROM DRAMACLUB 
            UNION {} SELECT FIRST_NAME FROM HIKECLUB
    )  SELECT COUNT(*) FROM all_clubs
    '''
# cumulative sizes of clubs (allowing double counting)
c = cur.execute(cte.format('ALL', 'ALL'))
ct_all = c.fetchone()
print('\ntotal size of 3 clubs:', ct_all[0])

# sum of students in clubs (no duplicates) 
d = cur.execute(cte.format('', ''))
ct_no_dupes = d.fetchone()
print('total # of students in 3 clubs:', ct_no_dupes[0])

con.commit()
con.close()