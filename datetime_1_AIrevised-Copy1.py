from tkinter import *
from tkinter import ttk
import datetime
import time
import calendar

master = Tk()
master.title("Digital Clock")

# Function to update time
#def get_time():
    #timevar = time.strftime("%I:%M:%S %p")
    #clock.config(text=timevar)
    #clock.after(200, get_time)

# Correcting clock label setup
#clock = Label(master, font=("Calibri", 70), bg="white", fg="black")
#clock.pack(fill="both")

#print date wiget
def full_cal():
    date = datetime.strftime.now(%m%d%Y)
    #datetime.label(font=("calibri", 10))
    date.config(text=date)

#  = label()    
         
# Start clock update
#get_time()
#full_cal()

master.mainloop()
