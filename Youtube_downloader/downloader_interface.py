from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk, Image

from urllib.request import urlopen
from io import BytesIO

root = Tk()

root.geometry("500x500")

text_box = Text(root, width=10, height=2, font = ("Helvetica", 20))

# Functions

def download():
    # link = text_box.get(1.0,END)

    # yt = YouTube(link)
    
    root.filename = filedialog.asksaveasfilename(title = "Save the file", filetypes = (("mp4 files","*.mp4"), ("all files","*.*")))
    
    # path = root.filename

    # YouTube(link).streams.first().download(root.filename)
    print(yt.streams)

    print(link)

# Checks the link

def check():

    link = text_box.get(1.0,END)
    yt = YouTube(link)
    
    # Video title
    url = yt.thumbnail_url
    # with urlopen(url) as thumbnail
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))

    yt_title = Label(root, text = yt.title)
    yt_title.grid(row = 5)

    # Video thumbnail

    yt_thb = ImageTk.PhotoImage(im)
    yt_thb_label = Label(root, image = yt_thb)

    yt_thb_label.grid(row = 6)




label_1 = Label(root, text = "Welcome to TheBestDownloader")
label_2 = Label(root, text = "Insert your link here")
download_button = Button(root, text = "Download", command = download)
check_button = Button(root, text = "Check Link", command = check)

text_box.grid(row = 2)
label_1.grid(row = 0)
label_2.grid(row = 1)
download_button.grid(row= 3)
check_button.grid(row= 4)

root.mainloop()