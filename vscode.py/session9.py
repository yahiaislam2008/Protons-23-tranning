import os 
import shutil
s=os.getcwd()
years=["2018","2019","2020","2021","2022","2023"]
for i in range(2018,2024):
   os.mkdir("o"+str(i))
data=os.listdir("C:\\Users\\CAVO TECH\\Downloads\\musicalbeeps-0.2.9\\data\\pics")
for h in data:
    for e in years:
        if e in h:
            shutil.copy(f"C:\\Users\\CAVO TECH\\Downloads\\musicalbeeps-0.2.9\\data\\pics\\{h}",f"C:\\Users\\CAVO TECH\\Downloads\\musicalbeeps-0.2.9\\images11\\{e}")

