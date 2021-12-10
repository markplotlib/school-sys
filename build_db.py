# build a database (create Connection object representing database)
import sqlite3
import os
from time import time

# filenames
dbfile = 'school-sys.db'
sql_filename = 'treehouse.sql'

if os.path.exists(dbfile):
    key = input('Database file exists. Copy? Overwrite? Abort? (c/o/A): ')
    if key.lower() == 'c':
        dbfile = 'copy-' + dbfile
    elif key.lower() == 'o':
        os.remove(dbfile)
    else:
        print('Program aborted.')
        quit()

con = sqlite3.connect(dbfile)

# create a cursor object
cur = con.cursor()

# DDL & insertions
sql_file = open(sql_filename)
sql_as_string = sql_file.read()

# takes about a half minute to build database
starttime = time()
cur.executescript(sql_as_string)
print('build_db took %.2f seconds' % (time() - starttime))

con.commit()
con.close()