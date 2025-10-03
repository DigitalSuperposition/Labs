from tkinter import *
from tkinter import ttk
from datetime import datetime  # Better import
import time
import calendar

master = Tk()
master.title("Digital Clock")

def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(1000, get_time)

# Create clock label - uncomment this!
clock = Label(master, font=("Calibri", 70), bg="white", fg="black")
clock.pack(fill="both")

def get_cal():
    # calendar.calendar() returns string, need to create Label
    cal_text = calendar.calendar(datetime.now().year)
    cal_label = Label(master, text=cal_text, font=("Courier", 10))
    
    # Format current date
    current_date = datetime.now().strftime("%m/%d/%Y")
    date_label = Label(master, text=current_date, font=("Calibri", 20))
    
    # Pack widgets
    cal_label.pack(side='bottom', fill='both')
    date_label.pack()

# Start updates
get_time()
get_cal()

master.mainloop()
