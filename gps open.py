import os
import openpyxl
from tkinter import filedialog
from tkinter import Tk
root=Tk()
root.withdraw()
file =  filedialog.askopenfilenames(initialdir ="C:/",title = "choose your file")


wb =openpyxl.load_workbook(file[0])
sheet = wb.get_sheet_by_name('Sheet1')
km=0
speed=0
sheet.delete_rows(1)

for cell_obj in list(sheet.columns)[2]:
    km=cell_obj.value + km
    

speed=km/3600
print('%.2f KM 주행'%speed)
os.system("pause")