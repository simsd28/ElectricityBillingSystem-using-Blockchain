# Import Module
from tkinter import *
import tkinter as tk


# create root window
root = Tk()

# root window title and dimension
root.title("User : CONSUMER")

# Set geometry(widthxheight)
root.geometry('500x300')


lbl = Label(root, text = "Enter Consumed Units:")
lbl.grid(column =0,row = 0)

txt = Entry(root, width=10)
txt.grid(column =1,row = 0)


lbl2 = Label(root)
lbl2.grid(column =1,row = 1)
# function to display user text when
# button is clicked
def clicked():

	res = txt.get()
	lbl2.configure(text = res)

btn = Button(root, text = "Send",fg = "red", command=clicked)
btn.grid(column=2,row = 0)

lbl4 = Label(root, text = "Current Consumption :")
lbl4.grid(column =0, row = 1)

def paybill():
    f2=Frame()
    f2.grid()

    txt=Entry(f2, width=10)
    txt.grid(column=0,row=3)

    btn2 = Button(f2, text = "Pay",fg = "red")
    btn2.grid(column = 1, row = 3)

    lbl = Label(f2, text = "Remaining Balance")
    lbl.grid(column =0,row = 4)

f2=Frame()
f2.grid()

btn1 = Button(root, text = "Pay Bill",fg = "red", command=paybill)
btn1.grid()


# Execute Tkinter
root.mainloop()
