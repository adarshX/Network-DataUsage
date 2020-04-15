#import numpy as np 
from matplotlib import pyplot as plt 
import os
from datetime import datetime


filepath = 'd.txt'
file = open(filepath , 'r')


## date and time 
systime = datetime.now()
current_time = systime.strftime("%H:%M")
hrs =  int(current_time[0:2])	#time as int
mins = int(current_time[3:5])
year = systime.year
day = systime.strftime("%a")
date = systime.strftime("%d")
month = systime.strftime("%b")

## reading file 
network = file.readline(5)	#reading 5 bytes of data
for i in range(1,15):		#skip this lines because they're unecessary
	file.readline()
labels = file.readline()
labels = labels[1:24]


#reading actual usage data
data = {}
for i in range(16,24):
	pos = 0
	ch = file.readline()
	for j in range(3):
		h = int(ch[pos:pos+2])
		rx = float(ch[pos+7:pos+13])
		tx = float(ch[pos+21:pos+25])
		pos = pos + 28
		total_data = rx + tx 
		total_data = round(total_data * 1.04 , 2)     #MiB to MB conversion
		data[h] = total_data
		


def string_rotate(input,d): 
   # Slice string in two parts (here we use left string) 
   first = input[0 : d] 
   second = input[d :] 
   rotated_string = second + first
   return rotated_string

def datalabels(x,y):
	for i , j in zip(x,y):
		label = j
		plt.annotate(label ,(i,j) ,textcoords="offset points",xytext=(0,5), ha='center')





## today data usage plot
fig1 = plt.figure(figsize=(16.0, 12.0))	#for full screen resolution
x = list(data.keys())
x.sort()
x2 = [i for i in range(0,hrs+1)]
datatoday = {key : data[key] for key in x2}
x2 = [str(h) +str(':00-') +  str(h+1) + str(":00") for h in x2]
Y = list(datatoday.values())
plt.bar(x2,Y,color = 'g',width = 0.6)
plt.xticks(rotation=-45 , fontsize = 7.5,fontweight="bold")
datalabels(x2,Y)
plt.title(f"Data usage Today ({date} {month} {year})  ",fontsize = 16 ,fontweight="bold" )
plt.xlabel("time inetrval")
plt.ylabel("Data used in MB",fontweight="bold")



#total data value
datausage = round(sum(Y),2)
print(date,month,year, ":Total data used today(wlo1 network) =", datausage , "MB")
plt.text(1 , max(Y)/2 , f"Data used today = {datausage} MB" , fontsize = 14 ,   color = 'orange',fontname='Comic Sans MS',bbox=dict(facecolor='none', edgecolor='violet'))
file.close()
os.remove(filepath)
plt.show()
