from tkinter import *
from bs4.element import Tag
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk, Image

import urllib.parse
import requests
import re

root = Tk()
root.geometry("500x500")

# Title 
root.title("Cat's Youtube Downloader")



"""
    Objectives:

    1) Make previous labels disappear, so I can put new ones (doing) 
    2) Save the VIDEOFILE into a correct filepath (X)
    3) Progress bar (ON TERMINAL) 
    4) How do I put a list into a display menu WHERE I can choose different options
    5) What does each point thing after each point mean? How Do I read that?
    6) How to read code?
    7) How to use the re package
    8) change VIDEOFILE name and format to WHATEVER I want
    9) Make a PROGRESS BAR

"""

# Text box

text_box = Text(root, width=40, height=0.5, font = ("Helvetica", 15))

# Variable to keep track of the option
# selected in OptionMenu
value_inside = StringVar(root)
value_inside.set("Select an Option")


# Functions

def download():

    directory = filedialog.askdirectory()
       
    # Exception

    if directory is None:
        return

    link = text_box.get(1.0,END)    
 
    yt = YouTube(link)

    # path = root.filename

    video =  YouTube(link).streams.first()
    # print(yt.streams)

    stream_option = value_inside.get()
    search = re.search('"(.*?)"', stream_option)

    if search:
        itag = int(search.group()[1:-1])
    else:
        return
    
    print("itag= ", itag)

    stream = yt.streams.get_by_itag(itag)
    video.download(directory)

    print("Download Completed")
    print("The video was DOWNLOADED TO: ", directory)

# Checks the link

def check():

    # Clear previous image
    # yt_thb_label['image'] = None

    link = text_box.get(1.0,END)
    yt = YouTube(link)
    
    # Video title
    yt_title = Label(root, text = yt.title)
    yt_title.pack()

    # Video thumbnail
    url = yt.thumbnail_url

    resp = requests.get(url, stream = True).raw
    im = Image.open(resp)
    # Resize 
    resized = im.resize((320, 180), Image.ANTIALIAS)

    yt_thb_label = Label(root)
    yt_thb_label.image = ImageTk.PhotoImage(resized)
    yt_thb_label['image'] = yt_thb_label.image

    yt_thb_label.pack()

    # Display menu with all the STREAM options
    stream_list = list(yt.streams.filter(file_extension='mp4'))
    option_menu = OptionMenu(root, value_inside, *stream_list)
    option_menu.pack()

# Text 

label_1 = Label(root, text = "Welcome to TheBestDownloader")
label_2 = Label(root, text = "Insert your link here")
download_button = Button(root, text = "Download", command = download)
check_button = Button(root, text = "Check Link", command = check)

# text_box.grid(row = 2)
# label_1.grid(row = 0)
# label_2.grid(row = 1)
# download_button.grid(row= 3)
# check_button.grid(row= 4)


label_2.pack()
text_box.pack()
label_1.pack()
download_button.pack()
check_button.pack()

# Everything
root.mainloop()