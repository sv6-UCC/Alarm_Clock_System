import time 

PARAM_ERROR = "Unsuitable parameter"

gmt = time.strftime('%H:%M:%S %p')
int(gmt[0:2])+1
world_times = {"gmt+1":int(gmt[0:2])+1, "gmt+2":int(gmt[0:2])+2, "gmt+3":int(gmt[0:2])+3, "gmt+4":int(gmt[0:2])+4,"gmt+5":int(gmt[0:2])+5, "gmt+6":int(gmt[0:2])+6,
        "gmt+7":int(gmt[0:2])+7, "gmt+8":int(gmt[0:2])+8,"gmt+9":int(gmt[0:2])+9, "gmt+10":int(gmt[0:2])+10, "gmt+11":int(gmt[0:2])+11, "gmt+12":int(gmt[0:2])+12,
        "gmt-1":int(gmt[0:2])-1, "gmt-2":int(gmt[0:2])-2, "gmt-3":int(gmt[0:2])-3, "gmt-4":int(gmt[0:2])-4,"gmt-5":int(gmt[0:2])-5, "gmt-6":int(gmt[0:2])-6,
        "gmt-7":int(gmt[0:2])-7, "gmt-8":int(gmt[0:2])-8,"gmt-9":int(gmt[0:2])-9, "gmt-10":int(gmt[0:2])-10, "gmt-11":int(gmt[0:2])-11, "gmt-12":int(gmt[0:2])-12}

def getTime(timezone):
    if timezone in world_times:
        hour = str(world_times[timezone])
        print(time.strftime("{}:%M:%S %p").format(hour))
    else: 
        return PARAM_ERROR
    

getTime("gmt-4")