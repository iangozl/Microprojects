from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk, Image

import urllib.parse
import io
import requests

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
    # print(yt.streams)

    print(link)

# Checks the link

def check():

    link = text_box.get(1.0,END)
    yt = YouTube(link)
    
    # Video title
    yt_title = Label(root, text = yt.title)
    yt_title.pack()

    # Video thumbnail
    url = yt.thumbnail_url
 

    print(url)

    # try:
    resp = requests.get(url, stream = True).raw
    # raw_data = urllib.request.urlopen(url).read()
    im = Image.open(resp)
    yt_thb_label = Label(root)
    yt_thb_label.image = ImageTk.PhotoImage(im)
    yt_thb_label['image'] = yt_thb_label.image

    
    yt_thb_label.pack()


label_1 = Label(root, text = "Welcome to TheBestDownloader")
label_2 = Label(root, text = "Insert your link here")
download_button = Button(root, text = "Download", command = download)
check_button = Button(root, text = "Check Link", command = check)

# text_box.grid(row = 2)
# label_1.grid(row = 0)
# label_2.grid(row = 1)
# download_button.grid(row= 3)
# check_button.grid(row= 4)

text_box.pack()
label_1.pack()
label_2.pack()
download_button.pack()
check_button.pack()
root.mainloop()