import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# Do any teachers teach multiple subjects? If so, which teachers?
q_b = '''
WITH class_teachers AS
    (SELECT c.TEACHER_ID, t.*
            , s.NAME AS SUBJECT_NAME
            , c.SUBJECT_ID
    FROM    TEACHERS AS t
    JOIN    CLASSES AS c
        ON  c.TEACHER_ID = t.ID
    JOIN    SUBJECTS AS s
        ON  SUBJECT_ID = s.ID
    GROUP BY SUBJECT_ID)
SELECT  LAST_NAME, SUBJECT_NAME, SUBJECT_ID
FROM    class_teachers
WHERE   TEACHER_ID = (
    SELECT  TEACHER_ID
    FROM    class_teachers
    GROUP BY TEACHER_ID
    HAVING COUNT(TEACHER_ID) > 1)
'''

q_c = '''
WITH class_teachers AS
    (SELECT c.TEACHER_ID, t.*
            , s.NAME AS SUBJECT_NAME
            , c.SUBJECT_ID
    FROM    TEACHERS AS t
    JOIN    CLASSES AS c
        ON  c.TEACHER_ID = t.ID
    JOIN    SUBJECTS AS s
        ON  SUBJECT_ID = s.ID
    GROUP BY SUBJECT_ID)
SELECT  FIRST_NAME, LAST_NAME
FROM    class_teachers
GROUP BY TEACHER_ID
HAVING COUNT(TEACHER_ID) > 1
'''
print(cur.execute(q_c).fetchall())
print(cur.execute(q_b).fetchall())



# Treehouse solution 
qcheck = '''
SELECT DISTINCT FIRST_NAME,
                LAST_NAME,
                NAME AS "CLASS_NAME"
FROM TEACHERS
JOIN CLASSES ON TEACHERS.ID = CLASSES.TEACHER_ID
JOIN SUBJECTS ON SUBJECTS.ID = CLASSES.SUBJECT_ID
WHERE TEACHERS.ID IN
    (SELECT TEACHER_ID
     FROM CLASSES
     GROUP BY TEACHER_ID
     HAVING COUNT(DISTINCT SUBJECT_ID) > 1)
'''
print(cur.execute(qcheck).fetchall())

con.commit()
con.close()