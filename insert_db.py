# -*- coding: utf-8 -*-
import sqlite3 as lite

con = lite.connect('rpg_db.db')

with con:
    cur = con.cursor()
    cur.execute('select * from tbl_stats')
    result = cur.fetchall()

print result