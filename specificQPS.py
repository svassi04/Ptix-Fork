import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob

qpsRate=1
cpus=20
reps=5
find=0


for name in glob("./outputs/default_flags_smt_disabled_100-1000qps/cpuCState"):
    f=open(name, "r")
#f=open("cstate.txt", "r")
data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)
    
    #for item in row:
        #item = item.split()
        #data_array1.append(item)

#print(data_array1)
c0t = []
c1t = []
c1et = []
c6t = []
c0 = []
c1 = []
c1e = []
c6 = []
x = []
j=0
for i in range(len(data_array1)):
    if(len(data_array1[i]) == 4):
        if(float(str(data_array1[i][0]).replace("[","").replace(",",""))>1.00):
            c0t.append(float(str(data_array1[i][0]).replace("[","").replace(",","")))
            c1t.append(float(str(data_array1[i][1]).replace(",","")))
            c1et.append(float(str(data_array1[i][2]).replace(",","")))
            c6t.append(float(str(data_array1[i][3]).replace("]","")))
        else:
            x.append(int(int(j)/5+1)*qpsRate*100+j%5*5*qpsRate)
            j+=1
            c0.append(float(str(data_array1[i][0]).replace("[","").replace(",",""))*100.00)
            c1.append(float(str(data_array1[i][1]).replace(",",""))*100.00)
            c1e.append(float(str(data_array1[i][2]).replace(",",""))*100.00)
            tem=float(str(data_array1[i][3]).replace("]",""))
            if (tem>=0):
                c6.append(tem*100.00)
            else :
                c6.append(0)
                t=c0.pop(len(c0)-1)
                c0.append(float(t)*(1.00+tem))
                t=c1.pop(len(c0)-1)
                c1.append(float(t)*(1.00+tem))
                t=c1e.pop(len(c0)-1)
                c1e.append(float(t)*(1.00+tem))
        
        
#print(len(data_array1[0]))
print(len(c0), len(c1), len(c1e), len(c6), "\n")
#print("c0:",  c0, "\n\nc1:", c1, "\n\nc1e:", c1e, "\n\nc6:", c6)"
print((x))

# data from https://allisonhorst.github.io/palmerpenguins/

# create data

y1 = np.array(c0)
y2 = np.array(c1)
y3 = np.array(c1e)
y4 = np.array(c6)
 
# plot bars in stack manner
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y1[find*cpus*reps:(find+1)*cpus*reps], color='r', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y2[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps], color='b', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y3[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps]+y2[find*cpus*reps:(find+1)*cpus*reps], color='y', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y4[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps]+y2[find*cpus*reps:(find+1)*cpus*reps]+y3[find*cpus*reps:(find+1)*cpus*reps], color='g', width=qpsRate*2)
plt.xlabel("qps")
plt.ylabel("Time percentage(%) out of 30 sec in each C-state")
plt.legend(['c0', 'c1', 'c1e', 'c6'])
plt.title("Time percentage(%) out of 30 sec, in each C-state relative to qps")
plt.show()

y1 = np.array(c0t)
y2 = np.array(c1t)
y3 = np.array(c1et)
y4 = np.array(c6t)
 
# plot bars in stack manner
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y1[find*cpus*reps:(find+1)*cpus*reps], color='r', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y2[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps], color='b', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y3[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps]+y2[find*cpus*reps:(find+1)*cpus*reps], color='y', width=qpsRate*2)
plt.bar(x[0*cpus*reps:(0+1)*cpus*reps], y4[find*cpus*reps:(find+1)*cpus*reps], bottom=y1[find*cpus*reps:(find+1)*cpus*reps]+y2[find*cpus*reps:(find+1)*cpus*reps]+y3[find*cpus*reps:(find+1)*cpus*reps], color='g', width=qpsRate*2)
plt.xlabel("qps")
plt.ylabel("CState transitions in 30 sec in each C-state")
plt.legend(['c0', 'c1', 'c1e', 'c6'])
plt.title("CState transitions in 30 sec, in each C-state relative to qps")
plt.show()