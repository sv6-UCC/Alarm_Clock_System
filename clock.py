

from Alarm_clock.timer import *
from Alarm_clock.timeZones import *
from time import strftime


def wb():
    colour.config(bg="white", fg="black")
    clock.configure(bg="white", fg="black")

def pg():
    colour.config(bg="purple", fg="gold")
    clock.configure(bg="purple", fg="gold")


def gw():
    colour.configure(bg="green", fg="white")
    clock.configure(bg="green", fg="white")

def time():
    cur_time = strftime('%H:%M:%S %p')
    clock.config(text=cur_time, font=("new_roman", 50, "bold"))
    clock.after(1000, time)


root.title('Clock')
menu_bar = Menu(root)
menu_bar.configure(bg="orange")
menu_bar.add_cascade(label="Timer", command=run_timer)
menu_bar.add_command(label="Settings", command=manageSettings)
colour = Menu(menu_bar)
colour.add_command(label="Green & White", command=gw)
colour.add_command(label="Purple & Gold", command=pg)
colour.add_command(label="White & Black", command=wb)
colour.configure(activebackground="violet", activeforeground="blue")
menu_bar.add_cascade(label="Clock Colour", menu=colour)
menu_bar.add_command(label="Time Zones", command=run_tzs)
root.configure(menu=menu_bar)
clock = Label()
clock.pack()
time()
edit_time()

# if tmr._start:

mainloop()

