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
Label(frame1,text='Add Bus Details',fg='green3',font='Times 19 bold',borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=10,padx=w//4,pady=28)
Label(frame1,text=' ').grid(row=4,column=0,pady=10)
frame2=Frame(root)
frame2.grid(row=1,column=0,columnspan=10)
Label(frame2,text='Bus ID',font='Times 12 bold').grid(row=4,column=0,sticky=E)
b_id=Entry(frame2)
b_id.grid(row=4,column=1,sticky=W,padx=7)
Label(frame2,text='Bus Type',font='Times 12 bold').grid(row=4,column=2,sticky=E)
bus_type=StringVar()
bus_type.set("Bus Type")
option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2"]
Menu=OptionMenu(frame2,bus_type,*option)
Menu.grid(row=4,column=3,padx=10,sticky=W)
Label(frame2,text='Capacity',font='Times 12 bold').grid(row=4,column=4,sticky=E)
b_cap=Entry(frame2)
b_cap.grid(row=4,column=5,sticky=W,padx=7)
Label(frame2,text='Fare Rs',font='Times 12 bold').grid(row=4,column=6,sticky=E)
b_fare=Entry(frame2)
b_fare.grid(row=4,column=7,sticky=W,padx=7)
Label(frame2,text='Operator ID',font='Times 12 bold').grid(row=4,column=9,sticky=E,padx=5)
b_op_id=Entry(frame2)
b_op_id.grid(row=4,column=10,sticky=W,padx=10)
Label(frame2,text='Route ID',font='Times 12 bold').grid(row=4,column=11,sticky=E,padx=5)
b_route_id=Entry(frame2)
b_route_id.grid(row=4,column=12,sticky=W,padx=10)
def show():
    if(b_id.get()=='' or b_cap.get()=='' or b_fare.get()=='' or b_op_id.get()=='' or b_route_id.get()=='' or bus_type.get()=='Bus Type'):
        showerror('Error','Enter the complete details')
    else:
        show1()
def show2():
    if(b_id.get()=='' or b_cap.get()=='' or b_fare.get()=='' or b_op_id.get()=='' or b_route_id.get()=='' or bus_type.get()=='Bus Type'):
        showerror('Error','Enter the complete details')
    else:
        show3()
        
frame3=Frame(root)
frame3.grid(row=2,column=0,columnspan=10)

def show1():
    a=b_id.get()
    b=bus_type.get()
    c=b_cap.get()
    d=b_fare.get()
    e=b_op_id.get()
    f=b_route_id.get()
    x=(a,b,c,d,e,f)
    cur.execute('insert into Bus(B_id,B_type,Capacity,Fare,OP_ID,R_ID) values (?,?,?,?,?,?)',x)
    con.commit()
    
    
    Label(frame3,text=b_id.get(),font='Times 10 bold').grid(row=5,column=3,pady=20)
    Label(frame3,text=bus_type.get(),font='Times 10 bold').grid(row=5,column=4,sticky=W,pady=20)
    Label(frame3,text=b_cap.get(),font='Times 10 bold').grid(row=5,column=5,sticky=W,pady=20)
    Label(frame3,text=b_fare.get(),font='Times 10 bold').grid(row=5,column=6,sticky=W,pady=20)
    Label(frame3,text=b_op_id.get(),font='Times 10 bold').grid(row=5,column=7,sticky=W,pady=20)
    Label(frame3,text=b_route_id.get(),font='Times 10 bold').grid(row=5,column=8,sticky=W,pady=20)
    showinfo('Info','New Bus added successfully')
def show3():
    Label(frame3,text=b_id.get(),font='Times 10 bold').grid(row=5,column=3,pady=20)
    Label(frame3,text=bus_type.get(),font='Times 10 bold').grid(row=5,column=4,sticky=W,pady=20)
    Label(frame3,text=b_cap.get(),font='Times 10 bold').grid(row=5,column=5,sticky=W,pady=20)
    Label(frame3,text=b_fare.get(),font='Times 10 bold').grid(row=5,column=6,sticky=W,pady=20)
    Label(frame3,text=b_op_id.get(),font='Times 10 bold').grid(row=5,column=7,sticky=W,pady=20)
    Label(frame3,text=b_route_id.get(),font='Times 10 bold').grid(row=5,column=8,sticky=W,pady=20)
    showinfo('Info','Bus Edited successfully')
    
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
Button(frame2,text='Add Bus',font='Times 13 bold',bg='pale green',bd=2,command=show).grid(row=5,column=6,pady=40)
Button(frame2,text='Edit Bus',font='Times 13 bold',bg='pale green',bd=2,command=show2).grid(row=5,column=7,pady=40)


frame4=Frame(root)
frame4.grid(row=3,column=0,columnspan=10)
home=PhotoImage(file='.\\home.png')
Button(frame4,image=home,bg='pale green',bd=2,command=home_scr).grid(row=5,column=9,pady=30)
root.mainloop()
