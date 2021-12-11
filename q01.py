import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# Who are the busiest teachers?
q = '''
WITH class_teachers AS
    (SELECT  t.*
    FROM    TEACHERS AS t
    JOIN    CLASSES AS c
        ON  t.ID = c.TEACHER_ID)
, course_load AS 
    (SELECT *, COUNT(*) AS ct
    FROM    class_teachers
    GROUP BY ID)
SELECT * FROM course_load
WHERE ct = (SELECT MAX(ct) FROM course_load)
'''
ans = cur.execute(q).fetchall()
print('count, query:', len(ans))
i = 0
while i < 5:
    print(ans[i])
    i += 1

# Treehouse solution 
qcheck = '''
WITH CLASSES_TEACHERS AS
  (SELECT *
   FROM TEACHERS
   JOIN CLASSES ON TEACHERS.ID = CLASSES.TEACHER_ID)
SELECT TEACHER_ID, LAST_NAME, FIRST_NAME,
       COUNT(PERIOD_ID) AS NUM_PERIODS
FROM CLASSES_TEACHERS
GROUP BY TEACHER_ID
HAVING NUM_PERIODS = 7
'''
result = cur.execute(qcheck).fetchall()
print('\ncount, answer:', len(result))
i = 0
while i < 5:
    print(result[i])
    i += 1

con.commit()
con.close()