import random
from tkinter import *
from tkinter import  messagebox

mw = Tk()
mw.geometry("600x400")
mw.resizable(0,0)
mw.title("Password Generator")
label = Label(mw, text="Password Generator" , font=("Arial", 20, "bold", "underlined"))
label.grid(column=0, row=0)
mw.mainloop()
