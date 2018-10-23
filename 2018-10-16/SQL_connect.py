import sqlite3

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key ,name varchar(20))')
    cursor.execute('INSERT INTO user (id,name) VALUES (\'1\',\'\Michael\')')
    cursor.rowcoun()
    cursor.fetchall()
finally:
    cursor.close()
    conn.close()



