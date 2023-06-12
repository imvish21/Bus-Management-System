import sqlite3
con=sqlite3.Connection('Dummy_DB')
cur=con.cursor()
#cur.execute('create table Passenger(P_id int,Pname varchar(20),Date date,Mobile int)')
#cur.execute('insert into Passenger(P_id,Pname,Date,Mobile) values (1,"Viany","2022-10-11",1234567890),(2,"Vishal","2022-10-12",2345678910),(3,"Vikalp","2022-10-13",3456789120)')
#cur.execute('create table Bus(B_id number primary key,Bname varchar(20),Date date,Route_id int)')
cur.execute('insert into Bus(B_id,Bname,Date,Route_id) values (4,"Bus4","2022-10-14",4)')
con.commit()
