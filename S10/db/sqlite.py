# create a table
#
# ----table-----
# insert, update, select, delete

import sqlite3


db_file = 'chinook.db'
conn = sqlite3.connect(db_file)

res = conn.execute("select * from tracks")
# for row in res:
#     print(row)

conn.execute("update person set firstname = 'John' where id = 1")
conn.commit()