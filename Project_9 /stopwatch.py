from tkinter import *



window = Tk()
window.title("Stopwatch")

def start():
    start_button.grid_forget()
    stop_button.grid(row=1, columnspan=2, sticky="ew")


def stop():
    stop_button.grid_forget()
    start_button.grid(row=1, columnspan=2, sticky="ew")


label_1 = Label(window, width=6, font=("Arial", 100), text="00:00")
label_1.grid(row=0, columnspan=2)

start_button = Button(window, text="START", font=("Arial", 30), command=start, activebackground="#37C207")
stop_button = Button(window, text="STOP", font=("Arial", 30), command=stop, activebackground="#CE2F0D")

continue_button = Button(window, text="Reset", font=("Arial", 30))
reset_button = Button(window, text="Continue", font=("Arial", 30))

# manage buttons with grid
start_button.grid(row=1, columnspan=2, sticky="ew")
# continue_button.grid(row=2, column=0)
# reset_button.grid(row=2, column=1)


window.mainloop()

"""
documentation

# sticky="ew" - from east to west
# window.geometry("720x480")



"""
