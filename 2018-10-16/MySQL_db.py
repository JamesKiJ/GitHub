import pymysql,mysql.connector

con = mysql.connector.connect(user='root',password='password',database='test')
cursor = con.cursor()

try:
    cursor.execute('drop table if exists user')
    cursor.execute('create table user(id int primary key,name varchar(20),sorce int)')
    cursor.execute(r"insert into user values(1,'Ming',90)")

finally:
    cursor.close()
    con.commit()
    con.close()


con = pymysql.connect('localhost','root','test')
cursor =con.cursor()
cursor.execute(r"select * from user where id =%s",(1))
values = cursor.fetchall()
print(values)
cursor.close()
con.close()
