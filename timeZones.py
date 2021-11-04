import time 

gmt = time.time()
east = {"gmt1":gmt+3600, "gmt2":gmt+7200, "gmt3":gmt+10800, "gmt4":gmt+14400,"gmt5":gmt+18000, "gmt6":gmt+21600,"gmt7":gmt+25200, "gmt8":gmt+28800,"gmt9":gmt+32400, "gmt10":gmt+36000, "gmt11":gmt+39600, "gmt12":gmt+43200}
west = {"gmt1":gmt-3600, "gmt2":gmt-7200, "gmt3":gmt-10800, "gmt4":gmt-14400,"gmt5":gmt-18000, "gmt6":gmt-21600,"gmt7":gmt-25200, "gmt8":gmt-28800,"gmt9":gmt-32400, "gmt10":gmt-36000, "gmt11":gmt-39600, "gmt12":gmt-43200}

moscow = east["gmt3"]
dublin = gmt 
print("Moscow==> ",moscow)
print("Dublin==> ", dublin)

