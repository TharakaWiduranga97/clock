from tkinter import *
from tkinter.ttk import *
from time import strftime

window=Tk()
window.title("My Clock")

def time():
    string=strftime("%H:%M:%S  %p")
    label.config(text=string)
    label.after(1000,time)            # do again same function 1000 milliseconds(1 second)

label=Label(window,font=("Arial Bold",50),background="black",foreground="yellow")
label.grid(column=0,row=0)

time()

window.mainloop()