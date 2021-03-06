# Import Required Library
from tkinter import *
import datetime
import time
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from threading import *
import calendar
from time import gmtime, strftime
import time

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")


# Use Threading
def Threading():
    t1 = Thread(target=saveNewAlarmTime)
    t1.start()

def displayCurrentTimeZone():
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Time Zones")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="Greenwich Mean Time").pack()

    Label(newWindow,text="\nGMT: " + time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())).pack()


def saveNewAlarmTime():
    lines = [hour.get(),minute.get(),second.get()]
    with open('data.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write(' ')
    setAlarmTimeAndDate()

def setAlarmTimeAndDate():
    # Infinite Loop
    isValidDate = True
    try:
        datetime.datetime(int(year.get()), int(month.get()), int(day.get()))
    except ValueError:
        isValidDate = False

    if (isValidDate):
        print("Input date is valid ..")
        while True:
            # Set Alarm

            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
            # set_alarm_date = f"{day.get()}:{month.get()}:{year.get()}"

            # Wait for one seconds
            time.sleep(1)

            # Get current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, set_alarm_time)

            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                alarmActivated()
    else:
        print("Input date is not valid..")




def alarmActivated():
    snooze_time = 20
    print("Time to Wake up")
    Button(root, text="Deactivate Alarm", font=("Helvetica 15"), command=deactivateCurrentAlarm).pack(pady=20)
    Label(root, text="Snooze Time "+str(snooze_time)).pack()
    Button(root, text="Snooze", font=("Helvetica 15"), command=snooze).pack(pady=20)
    # Playing sound SND_FILENAME|SND_LOOP|SND_ASYNC
    # winsound.PlaySound("alarm-tone.wav", winsound.SND_FILENAME, winsound.SND_LOOP,winsound.SND_ASYNC)
    try:
        sound =new_track
    except:
        sound ="alarm-tone.wav"
    PlaySound(sound, SND_FILENAME | SND_LOOP | SND_ASYNC)

def snooze():
    PlaySound(None, SND_FILENAME)
    time.sleep(20)
    alarmActivated()
def deactivateCurrentAlarm():
    PlaySound(None, SND_FILENAME)
# Add Labels, Frame, Button, Optionmenus
def edit_time():
    Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
    Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

    frame = Frame(root)
    frame.pack()

    global hour
    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
             '08', '09', '10', '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', '24'
             )
    hour.set(hours[0])

    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    global minute
    minute = StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    minute.set(minutes[0])

    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    global second
    second = StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    second.set(seconds[0])

    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    Label(root, text="Set Date", font=("Helvetica 15 bold")).pack()

    date_frame = Frame(root)
    date_frame.pack()

    global day
    day = StringVar(root)
    days = ('00', '01', '02', '03', '04', '05', '06', '07',
             '08', '09', '10', '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', '24','25','26','27','28','29','30','31'
             )
    day.set(days[0])

    dys = OptionMenu(date_frame, day, *days)
    dys.pack(side=LEFT)

    global month
    month = StringVar(root)
    months = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12')
    month.set(months[0])

    mth = OptionMenu(date_frame, month, *months)
    mth.pack(side=LEFT)

    global year
    year = StringVar(root)
    years = ('2021', '2022', '2023', '2024', '2025', '2026', '2027',
               '2028', '2029')
    year.set(years[0])

    yrs = OptionMenu(date_frame, year, *years)
    yrs.pack(side=LEFT)


    Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

def manageSettings():
    settingsWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    settingsWindow.title("Settings")

    # sets the geometry of toplevel
    settingsWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Button(settingsWindow, text="Select Ringtone", font=("Helvetica 15"), command=selectRingtone).pack(pady=20)
    #Button(settingsWindow, text="Snooze Time", font=("Helvetica 15"), command=editSnoozeTime).pack(pady=20)
    Button(settingsWindow, text="Change Volume", font=("Helvetica 15"), command=displayVolume).pack(pady=20)


def selectRingtone():
    ringWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    ringWindow.title("Ringtones")
    ringWindow.geometry("200x200")
    Button(ringWindow, text="First Track", font=("Helvetica 15"), command=new_ringtone("alarm-tone.wav")).pack(
        pady=20)
    Button(ringWindow, text="Second Track", font=("Helvetica 15"), command=new_ringtone("alarm-tone2.wav")).pack(
        pady=20)

    Button(ringWindow, text="Third Track", font=("Helvetica 15"), command=new_ringtone("alarm-tone3.wav")).pack(
        pady=20)
    # sets the geometry of toplevel

def new_ringtone(track):
    lines = [track]
    with open('data.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write(' ')
    global new_track
    new_track = track

def displayVolume():
    volWindow = Toplevel(root)
    volWindow.title("Volume")
    volWindow.geometry("200x200")
    Button(volWindow, text="Increase by 25%", font=("Helvetica 15"), command=changeVolume(0.25)).pack(
        pady=20)
    Button(volWindow, text="Increase by 50%", font=("Helvetica 15"), command=changeVolume(0.5)).pack(
        pady=20)

    Button(volWindow, text="Increase by 75%", font=("Helvetica 15"), command=changeVolume(0.75)).pack(
        pady=20)
    # sets the geometry of toplevel
def changeVolume(factor):
    lines = ["Increased by",str(factor)," %"]
    with open('data.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write(' ')
    import wave, audioop

    with wave.open('alarm-tone.wav', 'rb') as wav:
        p = wav.getparams()
        new_track ='output.wav'
        with wave.open(new_track, 'wb') as audio:
            audio.setparams(p)
            frames = wav.readframes(p.nframes)
            audio.writeframesraw(audioop.mul(frames, p.sampwidth, factor))

    new_ringtone(new_track)