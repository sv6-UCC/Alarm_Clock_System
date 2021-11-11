import time
from tkinter import *
from Alarm_clock.alarm import *

PARAM_ERROR = "Unsuitable parameter"

gmt = time.strftime('%H:%M:%S %p')
int(gmt[0:2]) + 1
world_times = {"gmt+1": int(gmt[0:2]) + 1, "gmt+2": int(gmt[0:2]) + 2, "gmt+3": int(gmt[0:2]) + 3,
               "gmt+4": int(gmt[0:2]) + 4, "gmt+5": int(gmt[0:2]) + 5, "gmt+6": int(gmt[0:2]) + 6,
               "gmt+7": int(gmt[0:2]) + 7, "gmt+8": int(gmt[0:2]) + 8, "gmt+9": int(gmt[0:2]) + 9,
               "gmt+10": int(gmt[0:2]) + 10, "gmt+11": int(gmt[0:2]) + 11, "gmt+12": int(gmt[0:2]) + 12,
               "gmt-1": int(gmt[0:2]) - 1, "gmt-2": int(gmt[0:2]) - 2, "gmt-3": int(gmt[0:2]) - 3,
               "gmt-4": int(gmt[0:2]) - 4, "gmt-5": int(gmt[0:2]) - 5, "gmt-6": int(gmt[0:2]) - 6,
               "gmt-7": int(gmt[0:2]) - 7, "gmt-8": int(gmt[0:2]) - 8, "gmt-9": int(gmt[0:2]) - 9,
               "gmt-10": int(gmt[0:2]) - 10, "gmt-11": int(gmt[0:2]) - 11, "gmt-12": int(gmt[0:2]) - 12}




def gmt_m1():
    getTime("gmt-1")


def gmt_m2():
    getTime("gmt-2")


def gmt_m3():
    getTime("gmt-3")


def gmt_m4():
    getTime("gmt-4")


def gmt_m5():
    getTime("gmt-5")


def gmt_m6():
    getTime("gmt-6")


def gmt_m7():
    getTime("gmt-7")


def gmt_m8():
    getTime("gmt-8")


def gmt_m9():
    getTime("gmt-9")


def gmt_m10():
    getTime("gmt-10")


def gmt_m11():
    getTime("gmt-11")


def gmt_m12():
    getTime("gmt-12")

def gmt_p1():
    getTime("gmt+1")

def gmt_p2():
    getTime("gmt+2")

def gmt_p3():
    getTime("gmt+3")

def gmt_p4():
    getTime("gmt+4")

def gmt_p5():
    getTime("gmt+5")

def gmt_p6():
    getTime("gmt+6")

def gmt_p7():
    getTime("gmt+7")

def gmt_p8():
    getTime("gmt+8")

def gmt_p9():
    getTime("gmt+9")

def gmt_p10():
    getTime("gmt+10")

def gmt_p11():
    getTime("gmt+11")

def gmt_p12():
    getTime("gmt+12")


def getTime(timezone=0):
    if timezone != 0:
        global curr_timezone
        curr_timezone = timezone
    hour = str(world_times[curr_timezone])
    tme_zone = time.strftime("{}:%M:%S %p").format(hour)
    tme_z.config(text=tme_zone, font=("new_roman", 50, "bold"))
    tme_z.after(1000, getTime)



def run_tzs():
    window = Toplevel(root)
    window.title("Time Zones")
    m_bar = Menu(window)
    window.configure(menu=m_bar)
    tz = Menu(m_bar)
    tz.add_command(label="GMT + 1", command=gmt_p1)
    tz.add_command(label="GMT + 2", command=gmt_p2)
    tz.add_command(label="GMT + 3", command=gmt_p3)
    tz.add_command(label="GMT + 4", command=gmt_p4)
    tz.add_command(label="GMT + 5", command=gmt_p5)
    tz.add_command(label="GMT + 6", command=gmt_p6)
    tz.add_command(label="GMT + 7", command=gmt_p7)
    tz.add_command(label="GMT + 8", command=gmt_p8)
    tz.add_command(label="GMT + 9", command=gmt_p9)
    tz.add_command(label="GMT + 10", command=gmt_p10)
    tz.add_command(label="GMT + 11", command=gmt_p11)
    tz.add_command(label="GMT + 12", command=gmt_p12)
    tz.add_command(label="GMT - 1", command=gmt_m1)
    tz.add_command(label="GMT - 2", command=gmt_m2)
    tz.add_command(label="GMT - 3", command=gmt_m3)
    tz.add_command(label="GMT - 4", command=gmt_m4)
    tz.add_command(label="GMT - 5", command=gmt_m5)
    tz.add_command(label="GMT - 6", command=gmt_m6)
    tz.add_command(label="GMT - 7", command=gmt_m7)
    tz.add_command(label="GMT - 8", command=gmt_m8)
    tz.add_command(label="GMT - 9", command=gmt_m9)
    tz.add_command(label="GMT - 10", command=gmt_m10)
    tz.add_command(label="GMT - 11", command=gmt_m11)
    tz.add_command(label="GMT - 12", command=gmt_m12)
    m_bar.add_cascade(label="Times", menu=tz)
    global tme_z
    tme_z = Label()
    tme_z.pack()