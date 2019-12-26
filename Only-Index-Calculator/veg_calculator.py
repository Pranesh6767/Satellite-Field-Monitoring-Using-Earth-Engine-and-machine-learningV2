import pandas as pd
import math
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
	#evi = (float(nir) - float(red))/((float(nir) + (6*float(red)) - (7.5*float(blue))) +1)
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
max_evi = max(eviarr)
last_evi = eviarr[-1]
second_evi = eviarr[-2]
change_evi = 100*((last_evi- second_evi)/second_evi)
evi_year_average = eviarr[-1:-17:-1]
evi_year_average_value = sum(evi_year_average)/len(evi_year_average)
print("Average EVI : ",avg_evi)
print("Maximum EVI : ",max_evi)
print("Latest EVI value : ",last_evi)
print("Percentage change : ",change_evi)
print("Last year Average EVI : ",evi_year_average_value)



avg_ndwi = sum(ndwiarr)/len(ndwiarr)
max_ndwi = max(ndwiarr)
last_ndwi = ndwiarr[-1]
second_ndwi = ndwiarr[-2]
change_ndwi = 100*((last_ndwi- second_ndwi)/second_ndwi)
ndwi_year_average = ndwiarr[-1:-17:-1]
ndwi_year_average_value = sum(ndwi_year_average)/len(ndwi_year_average)
print("Average NDWI : ",avg_ndwi)
print("Maximum NDWI : ",max_ndwi)
print("Latest NDWI value : ",last_ndwi)
print("Percentage change : ",change_ndwi)
print("Last year Average NDWI : ",ndwi_year_average_value)


avg_msavi = sum(msaviarr)/len(msaviarr)
max_msavi = max(msaviarr)
last_msavi = msaviarr[-1]
second_msavi = msaviarr[-2]
change_msavi = 100*((last_msavi- second_msavi)/second_msavi)
msavi_year_average = msaviarr[-1:-17:-1]
msavi_year_average_value = sum(msavi_year_average)/len(msavi_year_average)
print("Average MSAVI : ",avg_msavi)
print("Maximum MSAVI : ",max_msavi)
print("Latest MSAVI value : ",last_msavi)
print("Percentage change : ",change_msavi)
print("Last year Average MSAVI : ",msavi_year_average_value)


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/HP/Downloads/",title = "choose your file",filetypes = (("csv files","*.csv"),("all files","*.*")))
print (root.filename)
root.withdraw()
csv_path = root.filename


df2 = pd.read_csv(csv_path)

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
print("Average Rainfall : ",avg_rainfall)






out_csv = csv_path[22:]
fieldnames = ['Date_1', 'NDVI_1', 'NDWI_1','MSAVI_1']
writer = csv.DictWriter(open(out_csv, mode='w'), fieldnames=fieldnames,lineterminator='\n')
writer.writeheader()

for i in range(0,(len(eviarr)-1)):
	writer.writerow({'Date_1': dates[i], 'NDVI_1': eviarr[i], 'NDWI_1': ndwiarr[i], 'MSAVI_1': msaviarr[i]})
print('File Successfully Exported')
print("Check your program directory")















print("_____________________Machine Learning Prediction_________________________________")

print("\n\n\n\n")
import pickle
filename = 'finalized_kmeans_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


Xnew = [[avg_evi,avg_ndwi,avg_msavi,avg_rainfall]]
# make a prediction
ynew = loaded_model.predict_proba(Xnew)
print(ynew)
cluster1 = ynew[0,0]
cluster2 = ynew[0,1]
cluster3 = ynew[0,2]
cluster4 = ynew[0,3]

arr = [cluster1,cluster2,cluster3,cluster4]
maximum = max(arr)
index = arr.index(maximum)

percentage_prediction = maximum*100

print("element is in  cluster :",index+1)
print("Probability : ",percentage_prediction," %")
print("\n\n\n\n")


print("_____________________Machine Learning Prediction_________________________________")

y = []


for i in range(len(eviarr)):
	y.append(i)


import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = y 
y1 = eviarr 
# plotting the line 1 points  
plt.plot(x1, y1, label = "NDVI") 
  
# line 2 points 
x2 = y 
y2 = ndwiarr 
# plotting the line 2 points  
plt.plot(x2, y2, label = "NDWI") 

x3 = y 
y3 = ndwiarr 
# plotting the line 2 points  
plt.plot(x3, y3, label = "MSAVI") 



# naming the x axis 
plt.xlabel('Time') 
# naming the y axis 
plt.ylabel('Index') 
# giving a title to my graph 
plt.title('Analytics') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 