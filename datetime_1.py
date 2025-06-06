#Python code for calendar and time:
from tkinter import *
import datetime
import sys
import time
import calendar

master = tkinter.Tk()
master.title("Digital Clock")

def get_time():
    timevar  = time.strftime("%I: %M: %S %p")
    clock.config(text=timevar)
    clock.after(200,get_time)
    
clock = Label(master, font ="calibri", 90, bg ="blue", fg=("grey"))
clock.pack(fill)

tkinter.label(master, font="calibri", 50,  bg= "grey", fg="white")

def full_cal
    calendar.calendar()
    datetime.now
    calendar.calendar(year, month, day)
tkinter.pack()

print(full_cal)

