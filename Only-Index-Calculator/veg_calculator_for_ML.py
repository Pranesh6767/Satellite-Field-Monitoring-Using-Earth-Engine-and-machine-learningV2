import pandas as pd
import math
import matplotlib.pyplot as plt
from  tkinter import *
from tkinter import filedialog
import csv



"""root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/HP/Downloads/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
print (root.filename)
root.withdraw()
csv_path = root.filename"""



df = pd.read_csv('C:/Users/HP/Downloads/f15.csv')
df2 = pd.read_csv('C:/Users/HP/Downloads/r15.csv')


x = 3
i = 0
t = []
ndwiarr =[]
msaviarr = []
eviarr = []
dates = []
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
	evi = (float(nir)-float(red))/(float(nir)+float(red))
	#evi = (float(nir) - float(red))/(float(nir) + 6*float(red) - 7.5*float(blue) +1)
	ndwi = (float(nir)-float(swir))/(float(nir)+float(swir))
	msavi = ((2*float(nir))+1-(math.sqrt(((2*float(nir)+1)*(2*float(nir)+1))-(8*((float(nir)-float(red)))))))/2
	i = i+1
	eviarr.append(evi)
	ndwiarr.append(ndwi)
	msaviarr.append(msavi)
	try:
		date = str(df.loc[i,'system:time_start'])
		dates.append(date)
	except:
		break

avg_evi = sum(eviarr)/len(eviarr)
y = []


for i in range(len(eviarr)):
	y.append(i)


max_evi = max(eviarr)
last_evi = eviarr[-1]
second_evi = eviarr[-2]
change_evi = 100*((last_evi- second_evi)/second_evi)
evi_year_average = eviarr[-1:-17:-1]
evi_year_average_value = sum(evi_year_average)/len(evi_year_average)
#print(avg_evi)
#print(max_evi)
#print(last_evi)
#print("Percentage change : ",change_evi)
#print(evi_year_average_value)


avg_ndwi = sum(ndwiarr)/len(ndwiarr)
max_ndwi = max(ndwiarr)
last_ndwi = ndwiarr[-1]
second_ndwi = ndwiarr[-2]
change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
ndwi_year_average = ndwiarr[-1:-17:-1]
ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)
#print(avg_ndwi)
#print(max_ndwi)
#print(last_ndwi)
#print("Percentage change : ",change_ndwi)
#print(ndwi_year_average_value)





avg_msavi = sum(msaviarr)/len(msaviarr)
max_msavi = max(msaviarr)
last_msavi = msaviarr[-1]
second_msavi = msaviarr[-2]
change_msavi = 100*((last_msavi- second_msavi)/second_msavi)
msavi_year_average = msaviarr[-1:-17:-1]
msavi_year_average_value = sum(msavi_year_average)/len(msavi_year_average)
#print(avg_msavi)
#print(max_msavi)
#print(last_msavi)
#print("Percentage change : ",change_msavi)
#print(msavi_year_average_value)





"""root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/HP/Downloads/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
print (root.filename)
root.withdraw()
csv_path = root.filename"""



i = 0
x = 4
rainfall = []
while(x):
	try:
		rain = (df2.loc[i,'precipitation'])
	except:
		break
	rain = float(rain)
	rainfall.append(rain)
	i = i+1
avg_rainfall = sum(rainfall)/len(rainfall)
#print(avg_rainfall)



#fields = [avg_evi,max_evi,last_evi,evi_year_average_value,avg_ndwi,max_ndwi,last_ndwi,ndwi_year_average_value,avg_msavi,max_msavi,last_msavi,msavi_year_average_value,avg_rainfall,0]

#fields=[]
with open('dataset_ml.csv', 'a') as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerow([avg_evi,max_evi,last_evi,evi_year_average_value,avg_ndwi,max_ndwi,last_ndwi,ndwi_year_average_value,avg_msavi,max_msavi,last_msavi,msavi_year_average_value,avg_rainfall,1,lon,lat])






























