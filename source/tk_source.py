# import tkinter
try:
    from tkinter import *
    import tkinter as tk
except ImportError:
    print('Unable to import tkinter.')


root = Tk()
canvas = Canvas(root, height=500, width=900)
canvas.pack

frame=Frame()
frame.place(relx=.3,rely=.1,relwidth=.9,relheight=.8)

label=Label(frame,text='Add data here!')
label.grid(row=0,column=1)

root.mainloop()