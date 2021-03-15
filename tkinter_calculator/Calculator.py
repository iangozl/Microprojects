import tkinter
import calculations

window = tkinter.Tk()

window.geometry("300x400")
window.title("End Of The World Calc")

# Functions

def test():
    text_box.insert(0,"This is a test")

# Buttons

plus_button = tkinter.Button(window, text = "+")

equals_button = tkinter.Button(window, text = "=", command = test)

# Pack

plus_button.pack()
equals_button.pack()


# Text Box
text_box = tkinter.Entry(window,  )

text_box.pack()

window.mainloop()