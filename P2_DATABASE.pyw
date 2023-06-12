import sqlite3
con=sqlite3.Connection('P2_DB')
cur=con.cursor()
cur.execute('create table student(Fname text(20),Lname text(20),Enrollment varchar(10) primary key,Email varchar(20),Degree char(20),Branch char(20),Phone number)')
#cur.execute('drop table student')
con.commit()
