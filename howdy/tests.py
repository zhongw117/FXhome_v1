# -*- coding: utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host = 'localhost',
                       user = 'root',
                       password = 'a',
                       db = 'expertniu',
                       charset = 'utf8mb4',
                       )

cursor = conn.cursor()
cursor.execute("select id, url, ask_title from crawling_test where 1")
row = cursor.fetchone()
while row!= None:
    print('Title id:', row[0], '\t link:', row[1], '\t Title:', row[2])
    row = cursor.fetchone()

cursor.close()
conn.close()