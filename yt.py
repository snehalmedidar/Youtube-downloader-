# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:50:47 2022

@author: Acer
"""

from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    
    SAVE_PATH = "C:/Users/Acer/Downloads"  
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(SAVE_PATH)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()