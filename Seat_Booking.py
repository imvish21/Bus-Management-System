from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('MY_DATABASE')
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
Label(root,text='To',font='Times 15 bold').grid(row=3,column=2,sticky=E)
to=Entry(root)
to.grid(row=3,column=3,sticky=W)
Label(root,text='From',font='Times 15 bold').grid(row=3,column=4,sticky=E)
fro=Entry(root)
fro.grid(row=3,column=5,sticky=W)
Label(root,text='Journey Date',font='Times 15 bold').grid(row=3,column=6,sticky=E)
journey=Entry(root)
journey.grid(row=3,column=7,sticky=W)

def show1(h):
    
    Label(root,text="Select Bus",font='Times 15 bold',fg='lime green').grid(row=4,column=2)
    Label(root,text="Operator",font='Times 15 bold',fg='lime green').grid(row=4,column=3)
    Label(root,text="Bus Type",font='Times 15 bold',fg='lime green').grid(row=4,column=4)
    Label(root,text="Available/Capacity",font='Times 15 bold',fg='lime green').grid(row=4,column=5)
    Label(root,text="Fare",font='Times 15 bold',fg='lime green').grid(row=4,column=6)
    t=to.get()
    f=fro.get()
    j=journey.get()
    cur.execute('select B_id,OP_ID,B_type,Capacity,Fare from Bus,Route,Runs where (Sname between ? and ?) and R_ID=Route_id and Run_date=? and Bus_id=B_id',(t,f,j))
    con.commit()
    e=cur.fetchall()
    
    for i in range(0,len(e)):
        bus_select=IntVar()
        Radiobutton(root,text=e[i][0],bg='sky blue',bd=2,font='Times 12 bold',indicatoron=0,command=lambda:show2(h,m),variable=bus_select,value=1).grid(row=5,column=2)
        a=Label(root,text=e[i][1],font='Times 12 bold').grid(row=5,column=3,pady=15)
        b=Label(root,text=e[i][2],font='Times 12 bold').grid(row=5,column=4,pady=15)
        c=Label(root,text=e[i][3],font='Times 12 bold').grid(row=5,column=5,pady=15)
        d=Label(root,text=e[i][4],font='Times 12 bold').grid(row=5,column=6,pady=15)
    h=int(e[i][4])
    m=int(e[i][0])
    #showinfo('info',f)  
    
def show2(h,m):
    Button(root,text="Proceed To Book",bg='lime green',bd=2,command=lambda:show3(h,m)).grid(row=5,column=8,pady=10,columnspan=10)
def show3(h,m):
    Label(root,text='Fill Passenger Details To Book The Bus Ticket',font='Times 17 bold',bg='light blue',fg='red').grid(row=7,column=0,columnspan=10,padx=w//4,pady=20)
    Label(root,text='Name',font='Times 8 bold').grid(row=8,column=0,sticky=E)
    pname=Entry(root)
    pname.grid(row=8,column=1,sticky=W)
    Label(root,text='Gender',font='Times 8 bold').grid(row=8,column=2)
    gen_type=StringVar()
    gen_type.set("Select Gender")
    option=["Male","Female","Other"]
    menu=OptionMenu(root,gen_type,*option)
    menu.grid(row=8,column=3)
    Label(root,text='No of Seats',font='Times 8 bold').grid(row=8,column=4,sticky=E)
    seats=Entry(root)
    seats.grid(row=8,column=5,sticky=W)
    Label(root,text='Mobile No.',font='Times 8 bold').grid(row=8,column=6,sticky=E)
    mobile=Entry(root)
    mobile.grid(row=8,column=7,sticky=W)
    Label(root,text='Age',font='Times 8 bold').grid(row=8,column=8,sticky=E)
    age=Entry(root)
    age.grid(row=8,column=9,sticky=W)
    hoe=Button(root,text='Book Seat',bg='medium sea green',font='Times 8 bold',bd=5,command=lambda:show4(pname,seats,mobile,age,h,gen_type,m))
    hoe.grid(row=8,column=10,sticky=W)

def show4(pname,seats,mobile,age,h,gen_type,m):
    if(pname.get()=="" or seats.get()=="" or age.get()=="" or mobile.get()=="" or int(seats.get())>30):
        showerror('Error','Enter the correct details')
    else:
        call(pname,seats,mobile,age,h,gen_type,m)
def call(pname,seats,mobile,age,h,gen_type,m):
    #showinfo('info',seats.get())
    i=int(seats.get())*(h)
    answer=askyesno(title='Confirm ticket',message='Total amount to be paid:Rs:'+str(i))
    if answer:
        p=int(mobile.get())
        q=pname.get()
        r=gen_type.get()
        s=int(seats.get())
        t=journey.get()
        u=m
        v=fro.get()
        w=to.get()
        x=(p,q,r,s,t,u,v,w)
        cur.execute('insert into Bookhistory(C_Phone,C_name,Gender,Total_seat,Book_date,Id_bus,Boarding,Destination) values (?,?,?,?,?,?,?,?)',x)
        #cur.execute('update Bus set Capacity=')
        con.commit()
        root.destroy()
        import bus_ticket
           
    
def show():
    if(to.get()=="" or fro.get()=="" or journey.get()==""):
        showerror('Error','Enter the complete details')
    else:
        show1(h)
'''def openNewWindow(pname,seats,mobile,age):
    newWindow=Toplevel(root)
    newWindow.title("Ticket Details")
    newWindow.geometry('%dx%d+0+0'%(w,h))
    truck=PhotoImage(file='.\\Bus_for_project.png')
    Label(newWindow,image=truck).grid(row=0,column=0,columnspan=10,padx=600)
    Label(newWindow,text='Online Bus Booking System',font='Times 25 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//4,pady=30)
    pn=pname.get()
    s=seats.get()
    m=mobile.get()
    a=age.get()
    fr=Frame(newWindow,relief='groove',bd=3)
    fr.grid(row=2,column=0,columnspan=10)
    Label(fr,text='Passenger:',font='Times 15 bold').grid(row=3,column=0,sticky=E)
    Label(fr,text=pn,font='Times 15 bold').grid(row=3,column=1,sticky=W,padx=15)
    Label(fr,text='Gender:',font='Times 15 bold').grid(row=3,column=2,sticky=E)
    Label(fr,text='No of seats:',font='Times 15 bold').grid(row=4,column=0,sticky=E)
    Label(fr,text=s,font='Times 15 bold').grid(row=4,column=1,columnspan=10,sticky=W)
    Label(fr,text='Phone:',font='Times 15 bold').grid(row=4,column=2,sticky=E)
    Label(fr,text=m,font='Times 15 bold').grid(row=4,column=3,sticky=W)
    Label(fr,text='Age:',font='Times 15 bold').grid(row=5,column=0,sticky=E)
    Label(fr,text=a,font='Times 15 bold').grid(row=5,column=1,sticky=W)
    
   
    
    
    
    
    newWindow.mainloop()'''
    
def home_scr():
    root.destroy()
    import Home_screen  
Button(root,text='Show Bus',bg='medium sea green',font='Times 12 bold',bd=5,command=show).grid(row=3,column=8,sticky=W)
home=PhotoImage(file='.\\home.png')
Button(root,image=home,bg='PaleGreen',bd=3,command=home_scr).grid(row=3,column=9,sticky=W)

    

       
root.mainloop()
