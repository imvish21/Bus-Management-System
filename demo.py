from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('Dummy_DB')
cur=con.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
glob=Label(root,image=bus)
glob.grid(row=0,column=0,columnspan=10,padx=w//4)
Label(root,text='\n\n').grid(row=1,column=0,columnspan=10,padx=w//4)
Label(root,text='Online Bus Booking System',font='Times 30 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//4)
Label(root,text='Enter Journey Details',font='Times 15 bold',bg='pale green',fg='green4').grid(row=2,column=0,columnspan=10,padx=100,pady=20)
Label(root,text='Bus Id',font='Times 15 bold').grid(row=3,column=2,sticky=E)
to=Entry(root)
to.grid(row=3,column=3,sticky=W)
Label(root,text='Bus Name',font='Times 15 bold').grid(row=3,column=4,sticky=E)
fro=Entry(root)
fro.grid(row=3,column=5,sticky=W)
Label(root,text='Date',font='Times 15 bold').grid(row=3,column=6,sticky=E)
journey=Entry(root)
journey.grid(row=3,column=7,sticky=W)
Label(root,text='Route_id',font='Times 15 bold').grid(row=3,column=8,sticky=E)
route=Entry(root)
route.grid(row=3,column=9,sticky=W)
'''def show_bus():
    t=to.get()
    f=fro.get()
    j=journey.get()
    r=route.get()
    x=(t,f,j,r)
   # query='insert into Bus(B_id,Bname,Date,Route_id) values (?,?,?,?)'
    #cur.execute(query,x)
    #res=cur.fetchall()
    #con.commit()
   
    try:
        #cur.execute('insert into Bus(B_id,Bname,Date,Route_id) values (?,?,?,?)',x)
        #con.commit()
        cur.execute('select * from Bus where Date=? and Route_id=?',(j,r))
        show1()
    except sqlite3.IntegrityError:
        showerror('Error','Bus not found')'''
def delete():
    g=to.get()
    cur.execute('DELETE from Bus where B_id=?',g)
    con.commit()
    
    


    
def show():
    if(to.get()=="" or fro.get()=="" or journey.get()=="" or route.get()==''):
        showerror('Error','Enter the complete details')
    else:
        delete()
'''def show1():
    Label(root,text="bUS ID",font='Times 15 bold',fg='lime green').grid(row=4,column=2)
    Label(root,text="Select Bus",font='Times 15 bold',fg='lime green').grid(row=4,column=3)
    Label(root,text="DATE",font='Times 15 bold',fg='lime green').grid(row=4,column=4)
    Label(root,text="ROUTE ID",font='Times 15 bold',fg='lime green').grid(row=4,column=5)
    #search()
    #def search():
    t=to.get()
    f=fro.get()
    j=journey.get()
    r=route.get()
    cur.execute('select * from Bus where Date=? and Route_id=?',(j,r))
    con.commit()
    e=cur.fetchall()
    for i in range(0,len(e)):
        Label(root,text=e[i][0],font='Times 10 bold').grid(row=5,column=2,pady=10)
        Label(root,text=e[i][1],font='Times 10 bold').grid(row=5,column=3,pady=10)
        Label(root,text=e[i][2],font='Times 10 bold').grid(row=5,column=4,pady=10)
        Label(root,text=e[i][3],font='Times 10 bold').grid(row=5,column=5,pady=10)'''
                
        
                
            
        
        
    #bus_select=IntVar()
    
    #Radiobutton(root,text="Bus 1",bg='sky blue',bd=2,font='Times 12 bold',indicatoron=0,variable=bus_select,value=1).grid(row=5,column=2)
    #Radiobutton(root,text="Bus 2",bg='sky blue',bd=2,font='Times 12 bold',indicatoron=0,variable=bus_select,value=2).grid(row=6,column=2,pady=15)
Button(root,text='Show Bus',bg='medium sea green',font='Times 12 bold',bd=5,command=show).grid(row=3,column=10,sticky=W)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='PaleGreen',bd=3).grid(row=5,column=9,sticky=W)
