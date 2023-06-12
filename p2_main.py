from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('P2_DB')
cur=con.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=10)
Label(fr1,text='\n\n*Student Data Record*\n\n',font='Times 30 bold',fg='Orange',bd=5).grid(row=0,column=0,padx=600)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=10)
Label(fr2,text='First Name',font='Times 12 bold').grid(row=1,column=0,sticky=E)
fname=Entry(fr2)
fname.grid(row=1,column=1,sticky=W,padx=8)
Label(fr2,text='Last Name',font='Times 12 bold').grid(row=1,column=2,sticky=E)
lname=Entry(fr2)
lname.grid(row=1,column=3,sticky=W,padx=8)
Label(fr2,text='Enrollment',font='Times 12 bold').grid(row=1,column=4,sticky=E)
eno=Entry(fr2)
eno.grid(row=1,column=5,sticky=W,padx=8)
Label(fr2,text='Email',font='Times 12 bold').grid(row=1,column=6,sticky=E)
email=Entry(fr2)
email.grid(row=1,column=7,sticky=W,padx=8)
Label(fr2,text='Degree',font='Times 12 bold').grid(row=1,column=8,sticky=E)
degree=StringVar()
degree.set("Select Degree")
option=["B.tech","M.tech"]
menu=OptionMenu(fr2,degree,*option)
menu.grid(row=1,column=9,sticky=W,padx=8)
Label(fr2,text='Course',font='Times 12 bold').grid(row=1,column=10,sticky=E)
course=StringVar()
course.set("Select Course")
option=["CSE","MECH","ECE"]
menu=OptionMenu(fr2,course,*option)
menu.grid(row=1,column=11,sticky=W,padx=10)
Label(fr2,text='Mobile',font='Times 12 bold').grid(row=1,column=12,sticky=E)
mob=Entry(fr2)
mob.grid(row=1,column=13,sticky=W,padx=8)
def show():
    if(fname.get()=='' or lname.get()=='' or eno.get()=='' or email.get()=='' or degree.get()=='Select Degree' or course.get()=='Select Course' or mob.get()==''):
        showerror('Error','Enter the complete Details')
    elif(int(mob.get())<1000000000 or int(mob.get())>9999999999):
        showerror('Error','Enter the correct mobile number')
    else:
        show1()
def show1():
    a=fname.get()
    b=lname.get()
    c=eno.get()
    d=email.get()
    e=degree.get()
    f=course.get()
    g=mob.get()
    x=(a,b,c,d,e,f,g)
    try:
        cur.execute('insert into student(Fname,Lname,Enrollment,Email,Degree,Branch,Phone) values (?,?,?,?,?,?,?)',x)
        con.commit()
        show2()
    except sqlite3.IntegrityError:
        showerror('Error','Enrollment Already Exist')
    '''except ValueError:
        showerror('Error','Wrong Input Type')'''
        
def show2():
    showinfo('Info','Data Recorded Successfully')
    Label(fr2,text=fname.get(),font='Times 10 bold').grid(row=2,column=3,sticky=E)
    Label(fr2,text=lname.get(),font='Times 10 bold').grid(row=2,column=4,sticky=W)
    Label(fr2,text=eno.get(),font='Times 10 bold').grid(row=2,column=5,sticky=W)
    Label(fr2,text=email.get(),font='Times 10 bold').grid(row=2,column=6,sticky=W)
    Label(fr2,text=degree.get(),font='Times 10 bold').grid(row=2,column=7,sticky=W)
    Label(fr2,text=course.get(),font='Times 10 bold').grid(row=2,column=8,sticky=W)
    Label(fr2,text=mob.get(),font='Times 10 bold').grid(row=2,column=9,sticky=W)
def on_closing():
    a=askyesno('Quit','Do you want to quit?')
    if a==True:
        root.destroy()
    elif a==False:
        return
    
root.protocol("WM_DELETE_WINDOW",on_closing)   
But=Button(fr2,text='ADD',font='Times 13 bold',bg='medium sea green',bd=5,command=show)
But.grid(row=1,column=14,sticky=W)


    
