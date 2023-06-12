from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,columnspan=10,padx=630)
Label(frame1,text='Online Bus Booking System',font='Times 25 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=10,padx=w//4)
Label(frame1,text='Add New Details To DataBase',fg='green3',font='Times 17 bold',borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=10,padx=w//4,pady=28)
def show1():
    root.destroy()
    import New_Operator
def show2():
    root.destroy()
    import New_Bus
def show3():
    root.destroy()
    import New_Route
def show4():
    root.destroy()
    import New_Run
def on_closing(e=1):
    a=askyesno("Quit", "Do you want to quit?")
    if(a==True):
        root.destroy()   
    elif(a==False):
        return
root.protocol("WM_DELETE_WINDOW", on_closing)
Button(frame1,text='New Operator',font='Times 12 bold',bd=2,bg='pale green',command=show1).grid(row=4,column=3,padx=5,pady=10)
Button(frame1,text='New Bus',font='Times 12 bold',bd=2,bg='tomato',command=show2).grid(row=4,column=4,padx=5)
Button(frame1,text='New Route',font='Times 12 bold',bd=2,bg='steelblue2',command=show3).grid(row=4,column=5,padx=5)
Button(frame1,text='New Run',font='Times 12 bold',bd=2,bg='pink3',command=show4).grid(row=4,column=6)
root.mainloop()
