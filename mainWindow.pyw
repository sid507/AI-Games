import pygame
import os
from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading

pygame.init()

def begin_flyingFace(*args):
	root.withdraw()
	os.system('pythonw flyingFace.py')
	root.deiconify()


def begin_playerGame(*args):
	root.withdraw()
	os.system('pythonw playerGame.py')
	root.deiconify()


def load_screen():
	progress['value'] = 25
	time.sleep(1)
	progress['value'] = 50
	time.sleep(1)
	progress['value'] = 75
	time.sleep(1)
	progress['value'] = 100
	progress.pack_forget()
	title.pack_forget()
	load.pack_forget()
	select.pack(anchor=NW)
	l3.pack(side=TOP, anchor="center")
	l1.pack(padx=45, side=LEFT)
	l1.bind("<Button-1>", begin_playerGame)
	l2.pack(padx=45, side=RIGHT)
	l2.bind("<Button-1>", begin_flyingFace)

	
root = Tk()
root.configure(bg="black")
root.geometry("720x480")
root.maxsize(720,480)
root.title("AI Games")
root.wm_iconbitmap("ai.ico")
title = Label(root,text="AI Game Heaven",font="consolas 40", fg="white", bg="black")
title.pack(pady=120)
load = Label(root, text="Loading...", font="consolas 25", fg="white", bg="black")
load.pack(side=TOP)
progress = Progressbar(root,orient=HORIZONTAL,length=600,mode='determinate')
progress.pack()
t1 = threading.Thread(target=load_screen)
t1.start()
select = Label(root,text="    Select AI Game",font="consolas 45", fg="white", bg="black")
pg = PhotoImage(file="playGame.png")
l1 = Label(root, image=pg, borderwidth=0)
ff = PhotoImage(file="flyFace.png")
l2 = Label(root, image=ff, borderwidth=0)
line = PhotoImage(file="FlyingFace/Line.png")
l3 = Label(root, image=line, borderwidth=2)
root.mainloop()


