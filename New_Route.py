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
Label(frame1,text='Add Bus Route Details',fg='green3',font='Times 19 bold',borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=10,padx=w//4,pady=28)
Label(frame1,text=' ').grid(row=4,column=0,pady=10)
frame2=Frame(root)
frame2.grid(row=1,column=0,columnspan=10)
Label(frame2,text='Route ID',font='Times 12 bold').grid(row=4,column=0,sticky=E)
route_id=Entry(frame2)
route_id.grid(row=4,column=1,sticky=W,padx=7)
Label(frame2,text='Station Name',font='Times 12 bold').grid(row=4,column=2,sticky=E)
st_name=Entry(frame2)
st_name.grid(row=4,column=3,sticky=W,padx=7)
Label(frame2,text='Station ID',font='Times 12 bold').grid(row=4,column=4,sticky=E)
st_id=Entry(frame2)
st_id.grid(row=4,column=5,sticky=W,padx=15)
def show():
    if(route_id.get()=='' or st_name.get()=='' or st_id.get()==''):
        showerror('Error','Enter the complete details')
    else:
        show1()
def show2():
    if(route_id.get()=='' or st_name.get()=='' or st_id.get()==''):
        showerror('Error','Enter the complete details')
    else:
        show3()
        
frame3=Frame(root)
frame3.grid(row=2,column=0,columnspan=10)

def show1():
    a=route_id.get()
    b=st_name.get()
    c=st_id.get()
    x=(a,b,c)
    cur.execute('insert into Route(Route_id,Sname,S_id) values (?,?,?)',x)
    con.commit()
    Label(frame3,text=route_id.get(),font='Times 10 bold').grid(row=5,column=3,pady=20)
    Label(frame3,text=st_name.get(),font='Times 10 bold').grid(row=5,column=4,sticky=W,pady=20)
    Label(frame3,text=st_id.get(),font='Times 10 bold').grid(row=5,column=5,sticky=W,pady=20)
    showinfo('Info','New Roue added successfully')
def show3():
    showinfo('Info','Route Deleted successfully')
    
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
Button(frame2,text='Add Route',font='Times 13 bold',bg='pale green',bd=2,command=show).grid(row=4,column=6,padx=15)
Button(frame2,text='Delete Route',font='Times 13 bold',bg='pale green',bd=2,fg='red',command=show2).grid(row=4,column=11)
frame4=Frame(root)
frame4.grid(row=3,column=0,columnspan=10)
home=PhotoImage(file='.\\home.png')
Button(frame4,image=home,bg='pale green',bd=2,command=home_scr).grid(row=5,column=6,pady=50)
root.mainloop()
