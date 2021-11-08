

from timer import *

from time import strftime


class Check:
    def __init__(self):
        self._start = False

    def set(self, new_start):
        self._start = new_start


def wb():
    colour.config(bg="white", fg="black")
    clock.configure(bg="white", fg="black")

def pg():
    colour.config(bg="purple", fg="gold")
    clock.configure(bg="purple", fg="gold")

# def strt():
#     tmr.set(True)
#
# def stp():
#     tmr.set(False)

def gw():
    colour.configure(bg="green", fg="white")
    clock.configure(bg="green", fg="white")

def time():
    cur_time = strftime('%H:%M:%S %p')
    clock.config(text=cur_time, font=("new_roman", 50, "bold"))
    clock.after(1000, time)



# tmr = Check()
root.title('Clock')
menu_bar = Menu(root)
menu_bar.configure(bg="orange")
menu_bar.add_cascade(label="Timer", command=run_timer)
menu_bar.add_command(label="Settings", command=manageSettings)
# timer_option = Menu(menu_bar)
# timer_option.add_command(label="Start", command=strt)
# timer_option.add_command(label="stop", command=stp)
colour = Menu(menu_bar)
colour.add_command(label="Green & White", command=gw)
colour.add_command(label="Purple & Gold", command=pg)
colour.add_command(label="White & Black", command=wb)
colour.configure(activebackground="violet", activeforeground="blue")
menu_bar.add_cascade(label="Clock Colour", menu=colour)
root.configure(menu=menu_bar)
clock = Label()
clock.pack()
time()
edit_time()

# if tmr._start:

mainloop()

