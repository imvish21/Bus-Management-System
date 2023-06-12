from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('MY_DATABASE')
cur=con.cursor()
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,columnspan=10,padx=630)
Label(frame1,text='Online Bus Booking System',font='Times 28 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//4)
Label(frame1,text='Add Bus Operator Details',fg='green3',font='Times 19 bold',borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=10,padx=w//4,pady=28)
Label(frame1,text=' ').grid(row=4,column=0,pady=10)
frame2=Frame(root)
frame2.grid(row=1,column=0,columnspan=10)
Label(frame2,text='Operator id',font='Times 12 bold').grid(row=4,column=0,sticky=E)
op_id=Entry(frame2)
op_id.grid(row=4,column=1,sticky=W,padx=7)
Label(frame2,text='Name',font='Times 12 bold').grid(row=4,column=2,sticky=E)
op_name=Entry(frame2)
op_name.grid(row=4,column=3,sticky=W,padx=7)
Label(frame2,text='Address',font='Times 12 bold').grid(row=4,column=4,sticky=E)
op_add=Entry(frame2)
op_add.grid(row=4,column=5,sticky=W,padx=7)
Label(frame2,text='Phone',font='Times 12 bold').grid(row=4,column=6,sticky=E)
op_phone=Entry(frame2)
op_phone.grid(row=4,column=7,sticky=W,padx=7)
Label(frame2,text='Email',font='Times 12 bold').grid(row=4,column=8,sticky=E,padx=5,)
op_email=Entry(frame2)
op_email.grid(row=4,column=9,sticky=W,padx=10)
def show():
    if(op_id.get()=='' or op_name.get()=='' or op_add.get()=='' or op_phone.get()=='' or op_email.get()==''):
        showerror('Error','Enter the complete details')
    else:
        show1()
def show2():
    if(op_id.get()=='' or op_name.get()=='' or op_add.get()=='' or op_phone.get()=='' or op_email.get()==''):
        showerror('Error','Enter the complete details')
    else:
        show3()
        
frame3=Frame(root)
frame3.grid(row=2,column=0,columnspan=10)

def show1():
    a=op_id.get()
    b=op_name.get()
    c=op_add.get()
    d=op_phone.get()
    e=op_email.get()
    x=(a,b,c,d,e)
    cur.execute('insert into Operator(Operator_id,O_name,Address,O_Pno,Email) values (?,?,?,?,?)',x)
    con.commit()
    Label(frame3,text=op_id.get(),font='Times 10 bold').grid(row=5,column=3,pady=20)
    Label(frame3,text=op_name.get(),font='Times 10 bold').grid(row=5,column=4,sticky=W,pady=20)
    Label(frame3,text=op_add.get(),font='Times 10 bold').grid(row=5,column=5,sticky=W,pady=20)
    Label(frame3,text=op_phone.get(),font='Times 10 bold').grid(row=5,column=6,sticky=W,pady=20)
    Label(frame3,text=op_email.get(),font='Times 10 bold').grid(row=5,column=7,sticky=W,pady=20)
    showinfo('Info','New Opereator added successfully')
def show3():
    Label(frame3,text=op_id.get(),font='Times 10 bold').grid(row=5,column=3,pady=20)
    Label(frame3,text=op_name.get(),font='Times 10 bold').grid(row=5,column=4,sticky=W)
    Label(frame3,text=op_add.get(),font='Times 10 bold').grid(row=5,column=5,sticky=W)
    Label(frame3,text=op_phone.get(),font='Times 10 bold').grid(row=5,column=6,sticky=W)
    Label(frame3,text=op_email.get(),font='Times 10 bold').grid(row=5,column=7,sticky=W)
    showinfo('Info','Opereator Edited successfully')
    
def on_closing(e=1):
    a=askyesno("Quit", "Do you want to quit?")
    if(a==True):
        root.destroy()   
    elif(a==False):
        return
def home_scr():
    root.destroy()
    import Home_screen

root.protocol("WM_DELETE_WINDOW", on_closing)
Button(frame2,text='Add',font='Times 13 bold',bg='pale green',bd=2,command=show).grid(row=4,column=10,padx=10)
Button(frame2,text='Edit',font='Times 13 bold',bg='pale green',bd=2,command=show2).grid(row=4,column=11)
home=PhotoImage(file='.\\home.png')
frame4=Frame(root)
frame4.grid(row=3,column=0,columnspan=10)
Button(frame4,image=home,bg='pale green',bd=2,command=home_scr).grid(row=6,column=8,pady=50)
root.mainloop()
