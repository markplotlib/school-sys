import sqlite3

# filenames
dbfile = 'school-sys.db'

# create connection and cursor object
con = sqlite3.connect(dbfile)
cur = con.cursor()

# What class does Janis Ambrose teach during each period?
# Be sure to include all 7 periods in your report!
q = '''
WITH period_class_subject_teacher AS (
    SELECT  *
    FROM    PERIODS AS p
    LEFT OUTER JOIN    CLASSES AS c
        ON  p.ID = c.PERIOD_ID
    LEFT OUTER JOIN    SUBJECTS AS s
        ON  s.ID = c.SUBJECT_ID
    LEFT OUTER JOIN    TEACHERS AS t
        ON  t.ID = c.TEACHER_ID
    LEFT OUTER JOIN    ROOMS AS r
        ON  r.ID = c.ROOM_ID
    WHERE   t.FIRST_NAME = 'Janis'
        AND t.LAST_NAME = 'Ambrose'
)
SELECT  p.ID, p.START_TIME
        , IFNULL(NAME, '') AS 'Subject'
        , IFNULL(ROOM_ID, '')
FROM    PERIODS AS p
LEFT OUTER JOIN period_class_subject_teacher
    ON  p.ID = PERIOD_ID
'''
result = cur.execute(q).fetchall()
for res in result:
    print(res)

# Treehouse solution 
qcheck = '''
WITH PERIOD_CLASS_SUBJECT_TEACHER AS
  (SELECT *
   FROM PERIODS
   LEFT OUTER JOIN CLASSES ON PERIOD_ID = PERIODS.ID
   LEFT OUTER JOIN SUBJECTS ON SUBJECT_ID = SUBJECTS.ID
   LEFT OUTER JOIN TEACHERS ON TEACHER_ID = TEACHERS.ID
   WHERE FIRST_NAME = "Janis"
     AND LAST_NAME = "Ambrose" )
SELECT PERIODS.ID AS "Period No.",
       ROOM_ID,
       NAME AS "Subjects_Janis_Teaches"
FROM PERIODS
LEFT OUTER JOIN PERIOD_CLASS_SUBJECT_TEACHER ON PERIODS.ID = PERIOD_ID;
'''
answer = cur.execute(qcheck).fetchall()
print()
for ans in answer:
    print(ans)

con.commit()
con.close()