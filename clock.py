import sys
from  tkinter import *
import time

def time():
    current_time = time.srfime("%H:%M:%S")
    clock.config(text = current_time)
    cock.after(200,times)

root = tk()
root.geometry("500*250")
clock = Label (root, font = ("times", 50, "bold"),bg  = "white")
clock.grid(row = 2, column = 2, pady = 25, padx = 100)
times()

digi = Label(root, text = "Digital clock", font = "times 24 bold")
digi.grid(row = 0, column = 2)

nota = Label (root, tex = "hours       minutes     seconds    ",font = "time 15 bold")
nota.grid(row = 3, column = 2)

root.mainloop()