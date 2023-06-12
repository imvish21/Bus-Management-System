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
Label(frame1,text='Online Bus Booking System',font='Times 25 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//4)
Label(frame1,text='\n').grid(row=2,column=0,columnspan=10,padx=w//4)
Label(frame1,text='Check Your Booking',font='Times 15 bold',bg='pale green',fg='forest green').grid(row=2,column=0,columnspan=10,padx=w//4,pady=15)
frame2=Frame(root)
frame2.grid(row=1,column=0,columnspan=10)
Label(frame2,text='Enter Your Mobile Number',font='Times 12 bold').grid(row=0,column=3,padx=20,sticky=E)
a=Entry(frame2)
a.grid(row=0,column=4,sticky=W)
p=a.get()
def show():
    if(a.get()==''):
        showerror('error','Enter the number')
    else:
        booked_ticket()
def booked_ticket():
        fr=Frame(root,relief='groove',bd=5)
        fr.grid(row=2,column=0,columnspan=10)
        Label(fr,text='Passenger:',font='Times 15 bold').grid(row=3,column=0)
        #Label(fr,text=pn,font='Times 15 bold').grid(row=3,column=1,sticky=W,padx=15)
        Label(fr,text='Gender:',font='Times 15 bold').grid(row=3,column=2)
        Label(fr,text='No of seats:',font='Times 15 bold').grid(row=4,column=0,)
        #Label(fr,text=s,font='Times 15 bold').grid(row=4,column=1,columnspan=10)
        Label(fr,text='Phone:',font='Times 15 bold').grid(row=4,column=2)
        #Label(fr,text=m,font='Times 15 bold').grid(row=4,column=3,sticky=W)
        Label(fr,text='Bus ID:',font='Times 15 bold').grid(row=5,column=0)
        Label(fr,text='Boarding Station:',font='Times 15 bold').grid(row=5,column=2)
        Label(fr,text='Destination:',font='Times 15 bold').grid(row=6,column=0)
        Label(fr,text='Date:',font='Times 15 bold').grid(row=6,column=2)
        #Label(fr,text=a,font='Times 15 bold').grid(row=5,column=1,sticky=W)
        cur.execute('select C_Phone,C_name,Gender,Total_seat,Book_date,Id_bus,Boarding,Destination from Bookhistory where C_Phone=?',p)
        con.commit()
        e=cur.fetchall()
        for i in range(0,len(e)):
            Label(fr,text=e[i][0],font='Times 10 bold').grid(row=4,column=3)
            Label(fr,text=e[i][1],font='Times 10 bold').grid(row=3,column=1)
            Label(fr,text=e[i][2],font='Times 10 bold').grid(row=3,column=3)
            Label(fr,text=e[i][3],font='Times 10 bold').grid(row=4,column=1)
            Label(fr,text=e[i][4],font='Times 10 bold').grid(row=6,column=3)
            Label(fr,text=e[i][5],font='Times 10 bold').grid(row=5,column=1)
            Label(fr,text=e[i][6],font='Times 10 bold').grid(row=5,column=3)
            Label(fr,text=e[i][7],font='Times 10 bold').grid(row=6,column=1)
    


def on_closing(e=1):
    a=askyesno("Quit", "Do you want to quit?")
    if(a==True):
        root.destroy()   
    elif(a==False):
        return
root.protocol("WM_DELETE_WINDOW", on_closing)
Button(frame2,text='Check Booking',font='Times 12 bold',bd=3,command=show).grid(row=0,column=5,padx=33,sticky=E,pady=20)
root.mainloop()
