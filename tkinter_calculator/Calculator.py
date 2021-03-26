from tkinter import *
import calculations

import sys, os

program_directory=sys.path[0]

root = Tk()

root.geometry("450x200")
root.title("Simple Calc")
root.resizable(0,0) # This functions don't allow the windows to be resized

icon = PhotoImage(file=os.path.join(program_directory,"sunglasses.png"))
root.iconphoto(False, icon)

# Functions

def click(number):
    #text_box.delete(0, END)
    text_box.insert(END, number)

def equals():
    global number_2 
    
    number_2 = float(text_box.get())

    text_box.delete(0, END)

    if operation == 0:
        result = number_1 + number_2

    if operation == 1:
        result = number_1 * number_2

    if operation == 2:
        result = number_1 - number_2

    if operation == 3:
        result = number_1 / number_2
    text_box.insert(0, result)

def add():
    number = float(text_box.get())
    
    global number_1
    global operation

    number_1 = number
    text_box.delete(0, END)
    operation = 0

def clear():
    text_box.delete(0,END)

def multiply():
    global number_1
    global operation
    number_1 = float(text_box.get())    
    text_box.delete(0,END)
    operation = 1

def subtract():
    global number_1
    global operation
    number_1 = float(text_box.get())
    text_box.delete(0,END)
    operation = 2

def divide():
    global number_1
    global operation
    number_1 = float(text_box.get())
    text_box.delete(0,END)
    operation = 3

# Buttons

add_button = Button(root, text = "+", command = add)
equals_button = Button(root, text = "=", command = equals, width= 15, bg='green', fg='white')
clear_button = Button(root, text = "C", command = clear)
multiply_button = Button(root, text= "x", command = multiply)
subtract_button = Button(root, text="-", command= subtract)
divide_button = Button(root, text="/", command= divide)

button1 = Button(root, text= "1", command = lambda: click(1))
button2 = Button(root, text= "2", command = lambda: click(2))
button3 = Button(root, text= "3", command = lambda: click(3))
button4 = Button(root, text= "4", command = lambda: click(4))
button5 = Button(root, text= "5", command = lambda: click(5))
button6 = Button(root, text= "6", command = lambda: click(6))
button7 = Button(root, text= "7", command = lambda: click(7))
button8 = Button(root, text= "8", command = lambda: click(8))
button9 = Button(root, text= "9", command = lambda: click(9))
button0 = Button(root, text= "0", command = lambda: click(0))

# Pack

clear_button.grid(row=1, column=6)
divide_button.grid(row=1, column=4)
multiply_button.grid(row=2, column=4)
subtract_button.grid(row=3, column=4)
add_button.grid(row=4, column=4)
equals_button.grid(row=4, column=5, columnspan= 2)

# button2.pack()

button9.grid(row=1, column=0)
button8.grid(row=1, column=1)
button7.grid(row=1, column=2)

button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)

button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)

button0.grid(row=4, column=0)

# Text Box
text_box = Entry(root, width=50)

text_box.grid(row = 0, columnspan = 6)

root.mainloop()