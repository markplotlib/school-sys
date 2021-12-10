# build a database (create Connection object representing database)
import sqlite3
import os

# filenames
dbfile = 'school-sys.db'
sql_filename = 'treehouse.sql'

if os.path.exists(dbfile):
    key = input('Overwrite school-sys.db? (Y/n): ')
    if key != 'n':
        os.remove(dbfile)
    else:
        dbfile = 'copy-' + dbfile

con = sqlite3.connect(dbfile)

# create a cursor object
cur = con.cursor()

# DDL & insertions
sql_file = open(sql_filename)
sql_as_string = sql_file.read()

# execution takes minutes to run
cur.executescript(sql_as_string)

con.commit()
con.close()