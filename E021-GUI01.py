#**************************************************************
# Date: 110722 / 120122                                                *
# Title: Area of a Triangle                                   *
# Programmer: BoredManager                                    *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
from tkinter import *
import math

def click():
    fInitialVelocity = 0
    fAcceleration = 9.8
    UsrInputHeight=inputentry1.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputHeight)
        icheck = 0
        computed_data1 = math.sqrt(fInitialVelocity**2 + (2*fAcceleration*cUserInput1))
    except:
        computed_data1 ='Input Error'

    outputdata1.insert(END,computed_data1)
    
def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    inputentry1.delete(0, END)

w = Tk()
w.title("My Ideal Gas Law App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label (w, text="Drop Height(meters):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Final Velocity(m/s^2):", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# - The following are the open questions regarding the GUI
#   window:
#   a.) How do you get the square root without using math function?
#       The commented line is causing an issue when mathematically
#       speaking the formula is correct.
