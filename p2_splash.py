from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).pack()
Label(root,text='\n\n\n\n\n').pack()
Label(root,text='**WELCOME STUDENTS**',font='times 50 bold',fg='red').pack()
def close(e=1):
    root.destroy()
    import p2_main

root.bind('<Motion>',close)
root.mainloop()
