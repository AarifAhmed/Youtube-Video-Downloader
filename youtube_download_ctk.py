from customtkinter import *
import tkinter as t
from pytube import YouTube
import os

window = CTk()
percent = StringVar()
text = StringVar()
window.geometry("500x500")
font = CTkFont(family='Times New Roman', size=17)
window.title("Youtube Video Downloader")
window.resizable(height=False, width=False)


def entry_get():
    global complete_label
    if (x.get()) == 1:
        try:
            new_entry = YouTube(str(entry.get()))
            video = new_entry.streams.filter(only_audio=True).first()
            destination = str(destination_entry.get())
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            complete_label.configure(text='Download Complete', text_color='Green')
        except:
            complete_label.configure(text='Download Error', text_color='Red')

    if (x.get()) == 2:
        try:
            url = YouTube(str(entry.get()))
            video = url.streams.get_highest_resolution()
            destination = str(destination_entry.get())
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
            complete_label.configure(text='Download Complete', text_color='Green')
        except:
            complete_label.configure(text='Download Error', text_color='Red')

    if (x.get()) == 0:
        complete_label.configure(text='Please Select A Valid File Type', text_color='Red')


window = CTk()
window.title('Youtube Video Downloader')
window.geometry('350x350')
window.resizable(width=False, height=False)
photo = t.PhotoImage(file='Photos/youtube_logo.png')

x = IntVar()

file_label = CTkLabel(window, text="Select File Format", font=font)
file_label.place(x=0, y=110)
radio_button = CTkRadioButton(window, text="Mp3", variable=x, value=1, command=lambda: entry_get, font=font)
radio_button.place(x=50, y=140)

radio_button2 = CTkRadioButton(window, text="Mp4", variable=x, value=2, command=lambda: entry_get, font=font)
radio_button2.place(x=50, y=180)
font2 = CTkFont('bold')
welcome_label = CTkLabel(window, text="Youtube Video Downloader", font=font2)
welcome_label.pack()

label = CTkLabel(window, text="Enter Youtube Video Link =", font=font)
label.place(x=0, y=30)

entry = CTkEntry(window)
entry.place(x=200, y=30)

download_label = CTkLabel(window, text="Enter Download Location =", font=font)
download_label.place(x=0, y=70)

destination_entry = CTkEntry(window)
destination_entry.place(x=200, y=70)

download_button = CTkButton(window, text="Download", command=entry_get, height=2, width=10, font=font)
download_button.place(x=110, y=230)

complete_label = CTkLabel(window, text='')
complete_label.place(x=0, y=290)

window.mainloop()

window.mainloop()
