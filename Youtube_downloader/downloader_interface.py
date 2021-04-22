import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

text_box = tk.Text(root, width=10, height=2, font = ("Helvetica", 20))

label_1 = tk.Label(root, text = "Welcome to TheBestDownloader")
label_2 = tk.Label(root, text = "Insert your link here")
download_button = tk.Button(root, text = "Download")

text_box.grid(row = 2)
label_1.grid(row = 0)
label_2.grid(row = 1)
download_button.grid(row= 3)

root.mainloop()