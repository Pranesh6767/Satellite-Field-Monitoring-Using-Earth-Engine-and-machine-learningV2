import pandas as pd
import math
import matplotlib.pyplot as plt
from  tkinter import *
from tkinter import filedialog
import csv


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/HP/Downloads/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
print (root.filename)
root.withdraw()
csv_path = root.filename




df = pd.read_csv(csv_path)

x = 3
i = 0

dates = []
ndwiarr =[]
df.head()
while(x):
	try:
		blue = (df.loc[i,'B2'])
		blue = blue.replace(',', '')
	except:
		break
	red = (df.loc[i,'B4'])
	red = red.replace(',', '')
	nir = (df.loc[i,'B5'])
	nir = nir.replace(',', '')
	swir = (df.loc[i,'B6'])
	swir = swir.replace(',', '')
	ndwi = (float(nir)-float(swir))/(float(nir)+float(swir))
	i = i+1
	ndwiarr.append(ndwi)
	try:
		date = str(df.loc[i,'system:time_start'])
		dates.append(date)
	except:
		break
avg_evi = sum(ndwiarr)/len(ndwiarr)


avg_ndwi = sum(ndwiarr)/len(ndwiarr)
max_ndwi = max(ndwiarr)
last_ndwi = ndwiarr[-1]
second_ndwi = ndwiarr[-2]
change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
ndwi_year_average = ndwiarr[-1:-17:-1]
ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)


