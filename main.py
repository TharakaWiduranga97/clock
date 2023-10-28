from tkinter import *
from tkinter.ttk import *
from time import strftime


window=Tk()
window.title("My Clock")

def time():
    string=strftime("%H:%M:%S  %p")
    label.config(text=string)
    label.after(1000,time)            # do again same function 1000 milliseconds(1 second)