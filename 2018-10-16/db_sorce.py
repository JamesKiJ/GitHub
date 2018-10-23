import os,sqlite3


db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key ,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values('A-002','Bart',62)")
cursor.execute(r"insert into user values('A-003','Lisa',78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low,high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

    except sqlite3.DatabaseError as err:
        print(err)

    else:
        cursor.execute('SELECT * FROM user WHERE score >=? and score <= ? ORDER BY score',(low,high))
        data = cursor.fetchall()
        return list(map(lambda x:x[1],data))

    finally:
        cursor.close()
        conn.commit()
        conn.close()

assert get_score_in(80,95) == ['Adam'],get_score_in(80,95)
assert get_score_in(60,80) == ['Bart','Lisa'],get_score_in(60,80)
assert get_score_in(60,100) == ['Bart','Lisa','Adam'],get_score_in(60,100)

print('Pass')






