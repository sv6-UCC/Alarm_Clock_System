import tkinter
from tkinter import *
import time
from Alarm_clock.alarm import *
from tkinter import font
from winsound import *


class Timer:
    def __init__(self, target_time):
        self.target_time = target_time

    def setTargetTime(self, new_time):
        print(new_time)
        self.target_time = new_time

    def getTargetTime(self):
        return self.target_time

    def log(self):
        return time.time()


class Counter:
    def __init__(self, i):
        self.i = i

    def setCounter(self, val):
        self.i = val

    def getCounter(self):
        return self.i

    def increment(self):
        self.i = self.i + 1


timer = Timer(1)
counter = Counter(0)


def play():
    PlaySound('timerSound.wav', SND_FILENAME)
    time.sleep(1)
    PlaySound('timerSound.wav', SND_FILENAME)


def convertToSeconds(hour, minute, second):
    shours = int(hour) * 3600
    sminutes = int(minute) * 60
    ssecond = int(second)
    total = shours + sminutes + ssecond
    timer.setTargetTime(total)


def stop():
    timer.setTargetTime(0)


def begin():
    hour = hours.get()
    minute = minutes.get()
    second = seconds.get()
    convertToSeconds(hour, minute, second)
    targetLabel["text"] = "Target Time: " + str(hour) + " : " + str(minute) + " : " + str(second)
    countdown()


def countdown():
    i = time.time()
    total_time = int(time.time()) + timer.getTargetTime()
    dtime = total_time - i
    # remainingLabel.grid()
    # remainingLabel["text"] = "Time Remaining in seconds: {}".format(dtime)
    while i < total_time:
        # print(total_time - i)
        # remainingLabel["text"] = "Time Remaining in seconds: {}".format(dtime)
        time.sleep(1)
        i += 1
    print("finished")
    play()

def run_timer():
    master = Toplevel(root)
    master.title("Timer")
    master.geometry("500x400")
    master.configure(bg="red")

    frame1 = Frame(master, bd=10, bg="black", relief="ridge")
    frame1.grid(column=1, row=1, padx=200)

    askLabel = Label(frame1, text="Enter Target time below:")
    askLabel.configure(width=21, bg="black", fg="white", font=5)
    askLabel.grid(column=1, row=2)

    global targetLabel
    targetLabel = Label(frame1, text="Target Time: ")
    targetLabel.configure(width=21, bg="black", fg="white")
    targetLabel.grid(column=1, row=5)

    startButton = Button(frame1, text="BEGIN", command=begin)
    startButton.configure(width=15, bg="white")
    startButton.grid(column=1, row=4, pady=20)

    stopButton = Button(frame1, text="STOP", command=stop)
    stopButton.configure(width=15, bg="white")
    stopButton.grid(column=1, row=5, pady=20)
    stopButton.grid_remove()

    remainingLabel = Label(frame1, text="Remaining Time: ")
    remainingLabel.configure(width=21, bg="black", fg="white")
    remainingLabel.grid(column=1, row=6)
    remainingLabel.grid_remove()

    frame2 = Frame(frame1, bd=10, bg="black")
    frame2.grid(column=1, row=3)

    hourLabel = Label(frame2, text="Hours")
    hourLabel.configure(width=10)
    hourLabel.grid(column=1, row=0)

    minuteLabel = Label(frame2, text="Minutes")
    minuteLabel.configure(width=10)
    minuteLabel.grid(column=2, row=0)

    secondLabel = Label(frame2, text="Seconds")
    secondLabel.configure(width=10)
    secondLabel.grid(column=3, row=0)

    global hours
    hours = Spinbox(frame2, from_=0, to=23, state="readonly")
    hours.configure(width=10)
    hours.grid(column=1, row=1)
    global minutes
    minutes = Spinbox(frame2, from_=0, to=59, state="readonly")
    minutes.configure(width=10)
    minutes.grid(column=2, row=1)
    global seconds
    seconds = Spinbox(frame2, from_=0, to=59, state="readonly")
    seconds.configure(width=10)
    seconds.grid(column=3, row=1)

    master.mainloop()