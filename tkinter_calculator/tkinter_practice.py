import tkinter

window = tkinter.Tk()
window.geometry("500x500")

def hello():
    print("Hello World!")

def characters():
    text = text_box.get()
    label["text"] = text



#Creating a label
label = tkinter.Label(window)
label.pack()

button1 = tkinter.Button(window, text = "Click me!", command = characters)
# Use lambda to use a function with parameters

text_box = tkinter.Entry(window, font = "Helvetica")
text_box.pack()

button1.pack() # Appears in the screen without a specific direction
 
window.mainloop() # This registers all that's happening inside the window

