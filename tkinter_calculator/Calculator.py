from tkinter import *
import calculations

root = Tk()

# root.geometry("300x400")
root.title("End Of The World Calc")

number_1 = 0
choice = 0
# Functions

def click(number):
    #text_box.delete(0, END)
    text_box.insert(END, number)

def equals():
    operations = [add, multiply]
    global number_2 = int(text_box.get())

    text_box.delete(0, END)

    result =  

    
    text_box.insert(0, result)    

def add():
    number = int(text_box.get())
    global number_1
    number_1 = number
    text_box.delete(0, END)
    return number_1 + number_2

def clear():
    text_box.delete(0,END)

def multiply():
    global number_1
    number_1 = text_box.get()
    text_box.delete(0,END)


# Buttons

add_button = Button(root, text = "+", command = add, width= 10)
equals_button = Button(root, text = "=", command = equals)
clear_button = Button(root, text = "C", command = clear)
multiply_button = Button(root, text= "x", command = multiply)

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

add_button.grid(row=4, column=1, columnspan = 2)
equals_button.grid(row=4, column=0)
# clear_button.pack()
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

# button0.grid(row = , column =)

# Text Box
text_box = Entry(root)

text_box.grid(row = 0, columnspan = 3)

root.mainloop()