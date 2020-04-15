import numpy as np 
from matplotlib import pyplot as plt 
import timeit as t
import os
from datetime import datetime
import pprint


filepath = 'd.txt'
file = open(filepath , 'r')


## time 
systime = datetime.now()
current_time = systime.strftime("%H:%M")
hrs =  int(current_time[0:2])	#time as int
mins = int(current_time[3:5])


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
		
#pprint.pprint(data)


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


## past 24 hours data usage plot
plt.figure(1)
x = list(data.keys())
x.sort()
x1 = string_rotate(x,hrs+1)
data24 = {key : data[key] for key in x1}
x1 = [str(h) +str(':00-') +  str(h+1) + str(":00") for h in x1]
y = list(data24.values())
plt.bar(x1,y,color = 'b',width = 0.6)
plt.xticks(rotation=-45 , fontsize = 7.5,fontweight="bold")
datalabels(x1,y)
plt.title("Data Usage over past 24 hours ",fontsize = 20,fontweight="bold")
plt.xlabel("time inetrval")
plt.ylabel("Data used in MB")
#plt.show(block = False)




file.close()
os.remove(filepath)
plt.show()
