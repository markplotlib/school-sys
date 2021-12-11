import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# Who are the busiest teachers?
q = '''
WITH busy AS
(
    SELECT  COUNT(*) AS load
            , t.ID || ': ' || t.LAST_NAME || ', ' || t.FIRST_NAME
    FROM    TEACHERS AS t
    JOIN    CLASSES AS c
        ON  t.ID = c.TEACHER_ID
    GROUP BY t.ID
    HAVING load = 7
)
SELECT * FROM busy
'''
ans = cur.execute(q).fetchall()
print('count, query:', len(ans))
print(ans, '\n\n')

qcheck = '''    -- solution from Treehouse teacher
WITH CLASSES_TEACHERS AS
  (SELECT *
   FROM TEACHERS
   JOIN CLASSES ON TEACHERS.ID = CLASSES.TEACHER_ID)
SELECT TEACHER_ID, LAST_NAME, FIRST_NAME,
       COUNT(PERIOD_ID) AS NUM_PERIODS
FROM CLASSES_TEACHERS
GROUP BY TEACHER_ID
HAVING NUM_PERIODS = 7;
'''
result = cur.execute(qcheck).fetchall()
print('count, answer:', len(result))
print(result)

con.commit()
con.close()