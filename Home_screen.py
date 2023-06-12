from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='\n\n').grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',font='Times 40 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='\n\n\n').grid(row=2,column=0,columnspan=10,padx=w//3)
def show1():
    root.destroy()
    import Seat_Booking
def show2():
    root.destroy()
    import check_booked_seat
def show3():
    root.destroy()
    import add_bus
Button(root,text='Seat Booking',font='Times 20 bold',bg='pale green',fg='black',command=show1).grid(row=3,column=4)
Button(root,text='Check Booked Seat',font='Times 20 bold',bg='pale green',fg='black',command=show2).grid(row=3,column=5)
Button(root,text='Add Bus Details',font='Times 20 bold',bg='pale green',fg='black',command=show3).grid(row=3,column=6)
Label(root,text='').grid(row=4,column=6)
Label(root,text='For Admin Only',font='Times 15 bold',fg='red').grid(row=5,column=6)
root.mainloop()
