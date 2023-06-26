"""
Stopwatch
using Tkinter module
"""

from tkinter import *
from datetime import datetime

temp = 0
after_id = ""

window = Tk()
window.title("Stopwatch")


def tick():
    global temp, after_id
    after_id = window.after(1000, tick)

    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label_1.config(text=str(f_temp))

    temp += 1


def start():
    start_button.grid_forget()
    stop_button.grid(row=1, columnspan=2, sticky="ew")
    tick()


def stop():
    stop_button.grid_forget()

    reset_button.grid(row=1, column=1, sticky="ew")
    continue_button.grid(row=1, column=0, sticky="ew")

    # cancel function
    window.after_cancel(after_id)


def cont():
    continue_button.grid_forget()
    reset_button.grid_forget()

    stop_button.grid(row=1, columnspan=2, sticky="ew")

    tick()


def rest():
    global temp
    temp = 0

    continue_button.grid_forget()
    reset_button.grid_forget()

    start_button.grid(row=1, columnspan=2, sticky="ew")
    label_1.config(text="00:00")


# back side above


# front side below
label_1 = Label(window, width=6, font=("Arial", 100), text="00:00")
label_1.grid(row=0, columnspan=2)

start_button = Button(window, text="START", font=("Arial", 30), command=start, activebackground="#37C207")
stop_button = Button(window, text="STOP", font=("Arial", 30), command=stop, activebackground="#CE2F0D")

continue_button = Button(window, text="Continue", font=("Arial", 30), command=cont, width=1, activebackground="#65FAF3")
reset_button = Button(window, text="Reset", font=("Arial", 30), command=rest, width=1, activebackground="#FABB65")

# manage buttons with grid
start_button.grid(row=1, columnspan=2, sticky="ew")

window.mainloop()

"""
documentation

# sticky="ew" - from east to west
# window.geometry("720x480")

# datetime.fromtimestamp(123456) ==> convert number to date
# strftime("%M:%S") ==> formated as ==> minutes:seconds


"""
