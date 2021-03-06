from tkinter import *
import sys, os
import math

program_directory=sys.path[0] # This is the path to this document

root = Tk()

root.geometry("530x350")
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
    text_box.delete(1.0, END)
    operation = 0

def clear():
    text_box.delete(1.0,END)

def multiply():
    global number_1
    global operation
    number_1 = float(text_box.get())    
    text_box.delete(1.0,END)
    operation = 1

def subtract():
    global number_1
    global operation
    number_1 = float(text_box.get())
    text_box.delete(1.0,END)
    operation = 2

def divide():
    global number_1
    global operation
    number_1 = float(text_box.get())
    text_box.delete(1.0,END)
    operation = 3

def power():
    global number_1
    number_1 = float(text_box.get()) ** 2
    text_box.delete(1.0,END)
    text_box.insert(1.0,number_1)

def square_root():
    global number_1
    number_1 = math.sqrt(float(text_box.get()))
    text_box.delete(1.0,END)
    text_box.insert(1.0,number_1)

def backspace():
    index_number = len(text_box.get()) - 1
    text_box.delete(index_number)

def equation():
    operation = text_box.get(1.0,END)
    
    if operation.find("("):
         operation = operation.replace("(", "*").replace(")","")
    
    print(operation)
    result = eval(operation)
    result2 = eval("(5)**2")

    print(result2)

    text_box.delete(1.0,END)
    text_box.insert(1.0,result)

# Buttons

equals_button = Button(root, text="=", command = equation, width= 18, height=3, bg='green', fg='white')
clear_button = Button(root, text="C", command = clear, width=7, height=3, bg='yellow')
subtract_button = Button(root, text="-", command= lambda: click(" - "), width=7, height=3)
divide_button = Button(root, text="/", command= lambda: click(" / "), width=7, height=3)
multiply_button = Button(root, text="x", command = lambda: click(" * "), width=7, height=3)
add_button = Button(root, text="+", command = lambda: click(" + "), width=7, height=3)
decimal_button = Button(root, text=".", command = lambda: click("."), width=7, height=3)
percentage_button = Button(root, text="%", width=7, height=3)
left_parenthesis_button = Button(root, text="(", command = lambda: click("("), width=7, height=3)
right_parenthesis_button = Button(root, text=")", command = lambda: click(")"), width=7, height=3)
power_button = Button(root, text="x²", command= lambda: click("**2") ,width=7, height=3)
sqrt_button = Button(root, text="√", command= lambda: click("**0.5") ,width=7, height=3)
backspace_button = Button(root, text="<-",command = backspace,width=7, height=3)

button1 = Button(root, text= "1", command = lambda: click(1), width=7, height=3)
button2 = Button(root, text= "2", command = lambda: click(2), width=7, height=3)
button3 = Button(root, text= "3", command = lambda: click(3), width=7, height=3)
button4 = Button(root, text= "4", command = lambda: click(4), width=7, height=3)
button5 = Button(root, text= "5", command = lambda: click(5), width=7, height=3)
button6 = Button(root, text= "6", command = lambda: click(6), width=7, height=3)
button7 = Button(root, text= "7", command = lambda: click(7), width=7, height=3)
button8 = Button(root, text= "8", command = lambda: click(8), width=7, height=3)
button9 = Button(root, text= "9", command = lambda: click(9), width=7, height=3)
button0 = Button(root, text= "0", command = lambda: click(0), width=7, height=3)

# Pack

clear_button.grid(row=1, column=5)
divide_button.grid(row=1, column=3)
multiply_button.grid(row=2, column=3)
subtract_button.grid(row=3, column=3)
add_button.grid(row=4, column=3)
equals_button.grid(row=4, column=4, columnspan= 2)
decimal_button.grid(row=4, column=1)
percentage_button.grid(row=4, column=2)
left_parenthesis_button.grid(row=2, column=4)
power_button.grid(row=3, column=4)
right_parenthesis_button.grid(row=2, column=5)
sqrt_button.grid(row=3, column=5)
backspace_button.grid(row=1, column=4)

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
text_box = Text(root, width=35, height=2, font = ("Helvetica", 20))

text_box.grid(row = 0, columnspan = 7)

root.mainloop()