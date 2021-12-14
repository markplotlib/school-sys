import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# 5) Which elective teacher is the most popular 
# (i.e., which teacher teaches the most students)?
q = '''
WITH mix AS (
    SELECT      COUNT(c.TEACHER_ID) AS ct
                , t.FIRST_NAME || ' ' || t.LAST_NAME AS "teacher"
                , subj.GRADE AS subject_grade
    FROM        CLASSES AS c
    JOIN        SUBJECTS AS subj
        ON      c.SUBJECT_ID = subj.ID
    JOIN        TEACHERS AS t
        ON      c.TEACHER_ID = t.ID
    JOIN        SCHEDULE AS sched
        ON      sched.CLASS_ID = c.ID
    JOIN        STUDENTS AS stud
        ON      sched.STUDENT_ID = stud.ID    
    WHERE       subject_grade IS NULL
    GROUP BY    TEACHER_ID
--    ORDER BY    subject_grade NULLS FIRST, ct DESC
)
SELECT  MAX(ct), teacher, subject_grade
FROM    mix
'''
result = cur.execute(q).fetchall()
print('{} teaches {} students \n(elective classes: grade = {}).'.format(result[0][1], result[0][0], result[0][2]))

# Treehouse solution 
qcheck = '''
SELECT TEACHERS.FIRST_NAME || " " || TEACHERS.LAST_NAME AS "Teacher",
       COUNT(SCHEDULE.STUDENT_ID) AS "Total_Student_Count"
FROM SUBJECTS
JOIN CLASSES ON CLASSES.SUBJECT_ID = SUBJECTS.ID
JOIN TEACHERS ON TEACHERS.ID = CLASSES.TEACHER_ID
JOIN SCHEDULE ON CLASSES.ID = SCHEDULE.CLASS_ID
WHERE SUBJECTS.GRADE IS NULL
GROUP BY CLASSES.TEACHER_ID
ORDER BY "Total_Student_Count" DESC
LIMIT 1;
'''
answer = cur.execute(qcheck).fetchall()
print()
for ans in answer:
    print(ans)

con.commit()
con.close()