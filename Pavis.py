import os
import json
from tkinter import filedialog
from tkinter import Tk
from tkinter.constants import TRUE

root=Tk()
root.withdraw()
a=0
daykm = 0
daytime=0
Twilightkm=0
Twiligtime=0
nightkm=0
nighttime=0
citykm=0
citytime=0
countryroadkm=0
countryroadtime=0
motorwaykm=0
motorwaytime=0

file =  filedialog.askopenfilenames(initialdir ="C:/",title = "JSON 선택")

while True:
    try:
        with open(file[a]) as file1:
            json_obj=json.load(file1)
            daykm += json_obj['Meta Information']['Day km']
            daytime += json_obj['Meta Information']['Day Time']
            Twilightkm += json_obj['Meta Information']['Twilight km']
            Twiligtime += json_obj['Meta Information']['Twilight Time']
            nightkm += json_obj['Meta Information']['Night km']
            nighttime += json_obj['Meta Information']['Night Time']
            citykm += json_obj['Meta Information']['City km']
            citytime += json_obj['Meta Information']['City Time']
            countryroadkm += json_obj['Meta Information']['Country Road km']
            countryroadtime += json_obj['Meta Information']['Country Road Time']
            motorwaykm += json_obj['Meta Information']['Motorway km']
            motorwaytime += json_obj['Meta Information']['Motorway Time']
        a += 1
        continue   

    except IndexError:
        daytime= daytime/3600
        Twiligtime= Twiligtime/3600
        nighttime = nighttime/3600
        citytime = citytime/3600
        countryroadtime = countryroadtime/3600
        motorwaytime = motorwaytime/3600

        print('day km = ' + str(round(daykm,2)) + 'Km')
        print('day time = ' + str(round(daytime,2)) + 'Hr')
        print('Twilight km = ' + str(round(Twilightkm,2)) + 'Km')
        print('Twilight Time = ' + str(round(Twiligtime,2)) + 'Hr')
        print('night Km = ' + str(round(nightkm,2)) + 'km')
        print('night time = ' + str(round(nighttime,2)) + 'Hr')
        print('city km = ' + str(round(citykm,2)) + 'km')
        print('city time = ' + str(round(citytime,2)) + 'Hr')
        print('countryroad km = ' + str(round(countryroadkm,2)) + 'Km')
        print('countryroad time = ' + str(round(countryroadtime,2)) + 'Hr')
        print('motorway km = ' + str(round(motorwaykm,2)) + 'km')
        print('motorway time = ' + str(round(motorwaytime,2)) + 'Hr')

        os.system("pause")
        break
        
