from tkinter import *
import customtkinter
from pytube import YouTube
from pytube import Search
import os

def main():

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.title("YouTube MP3 Downloader")
    root.geometry("340x120")

    website_entry = customtkinter.CTkEntry(master=root, placeholder_text="URL", width=340)
    website_entry.pack(padx=10, pady=10)
    website_entry.focus()
    root.resizable(False, False)

    def link_video():
        yt = YouTube(website_entry.get())
        name_video = customtkinter.CTkLabel(master=root, text=yt.title)
        name_video.pack(anchor=SW)
        name_video.place(x=15, y=40)
        yd = yt.streams.filter(only_audio=True).first()
        out_file = yd.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    button = customtkinter.CTkButton(master=root, width=36, height=36, text="Baixar Vídeo", command=link_video)
    button.place(x=134,y=70)

    root.mainloop()
    
if __name__ == '__main__':
    main()