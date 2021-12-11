import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# Which teachers don't have a class during 1st period?
q = '''
WITH free_teachers AS
(
    SELECT  c.PERIOD_ID
            , t.ID || ': ' || t.LAST_NAME || ', ' || t.FIRST_NAME
    FROM    CLASSES AS c
    JOIN    TEACHERS AS t
        ON  t.ID = c.TEACHER_ID
    GROUP BY t.ID
    HAVING  MIN(c.PERIOD_ID) != 1
)
SELECT * FROM free_teachers
LIMIT 3
'''
print(cur.execute(q).fetchall())

qcheck = '''    -- solution from Treehouse teacher
WITH free_teachers AS
  (SELECT TEACHERS.ID
   FROM TEACHERS
   WHERE TEACHERS.ID NOT IN
       (SELECT TEACHER_ID
        FROM CLASSES
        WHERE PERIOD_ID=1 ) )
SELECT free_teachers.ID,
       CLASSES.PERIOD_ID,
       TEACHERS.*
FROM free_teachers
JOIN CLASSES ON CLASSES.TEACHER_ID = free_teachers.ID
JOIN TEACHERS ON TEACHERS.ID = free_teachers.ID
'''
print('\n', cur.execute(qcheck).fetchall())

con.commit()
con.close()