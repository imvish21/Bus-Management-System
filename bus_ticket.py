from tkinter import *
from tkinter.messagebox import *
import sqlite3
con=sqlite3.Connection('MY_DATABASE')
cur=con.cursor()
root=Tk()
root.title("Online Bus Booking System")
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus_img=PhotoImage(file=".\\Bus_for_project.png")
l1=Label(image=bus_img)
l1.grid(row=0,column=0,padx=w//4,columnspan=10)
l2=Label(text="Online Bus Booking System",fg="red",font="Arial 20 bold")
l2.grid(row=1,column=0,padx=w//4,columnspan=10)
l2.config(bg="skyblue")
l3=Label(text="Bus Ticket",font="Arial 12 bold")
l3.grid(row=2,column=0,padx=w//3,columnspan=10,pady=20)
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
cur.execute('select C_Phone,C_name,Gender,Total_seat,Book_date,Id_bus,Boarding,Destination from Bookhistory where C_Phone=1234567890')
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
showinfo('Info','Seat booked successfully!!')
def on_closing(e=1):
    a=askyesnocancel("Quit", "Do you want to quit?")
    if(a==True):
        root.destroy()
    elif(a==False):
        root.destroy()
        import Home_screen
    elif(a is None):
        return
        
        

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
