import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# 4) Which subject is the least popular,
#    and how many students are taking it?
q = '''
WITH subj_class_sched_stud AS (
    SELECT  
            subj.ID     AS subj_id
            , subj.NAME AS subj_name
            -- , COUNT(subj.NAME) AS "STUDENT_COUNT"
            , stud.LAST_NAME AS "kid"
    FROM    SUBJECTS AS subj
    JOIN    CLASSES AS c
        ON  c.SUBJECT_ID = subj.ID
    JOIN    SCHEDULE
        ON  SCHEDULE.CLASS_ID = c.ID
    JOIN    STUDENTS AS stud
        ON  SCHEDULE.STUDENT_ID = stud.ID
)
SELECT      COUNT(subj_id) AS ct
            , subj_name
FROM        subj_class_sched_stud
GROUP BY    subj_id
ORDER BY    ct ASC
LIMIT 1
'''
result = cur.execute(q).fetchall()
print(result)

# Treehouse solution 
qcheck = '''
WITH CTE AS
  (SELECT NAME,
          COUNT(1) AS "STUDENT_COUNT"
   FROM SUBJECTS
   JOIN CLASSES ON SUBJECT_ID = SUBJECTS.ID
   JOIN SCHEDULE ON CLASS_ID = CLASSES.ID
   GROUP BY SUBJECT_ID)
SELECT NAME,
       MIN("STUDENT_COUNT")
FROM CTE;
'''
answer = cur.execute(qcheck).fetchall()
print()
for ans in answer:
    print(ans)

con.commit()
con.close()