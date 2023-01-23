import numpy as np
import csv
import matplotlib.pyplot as plt

f=open("output.txt", "r")
next(f)
next(f)
next(f)
data_array = []
for row in csv.reader(f):
    for item in row:
        item = item.split()
        data_array.append(item)



qps = []
qpsbar = []
AvLatency = []
TailLatency = []
reqpersec = []
totalreq = []
dropedreq = []
for i in range(len(data_array)):
    if(data_array[i][0]=="Latency" and data_array[i][1]!="Distribution"):
        if (data_array[i][1]!="-nanus"):
            tmp = str(data_array[i][1])
            if(tmp.find("ms")!=-1):
                AvLatency.append(float(str(data_array[i][1]).replace("ms",""))/1000)
            elif(tmp.find("us")!=-1):
                AvLatency.append(float(str(data_array[i][1]).replace("us",""))/1000000)
            elif(tmp.find("s")!=-1):
                AvLatency.append(float(str(data_array[i][1]).replace("s","")))
            else:
                print("error")
        else:
            AvLatency.append(0.00)

       #print(data_array[i][3])
        if (data_array[i][3]!="-nanus"):
            tmp = str(data_array[i][3])
            if(tmp.find("ms")!=-1):
                TailLatency.append(float(str(data_array[i][3]).replace("ms",""))/1000)
            elif(tmp.find("us")!=-1):
                TailLatency.append(float(str(data_array[i][3]).replace("us",""))/1000000)
            elif(tmp.find("s")!=-1):
                TailLatency.append(float(str(data_array[i][3]).replace("s","")))
            else:
                print("error")
       #AvLatency.append(str(data_array[i][1]).replace("ms",""))
       #TailLatency.append(str(data_array[i][3]).replace("ms",""))
    if(len(data_array[i])>1 and data_array[i][1]== "requests" and data_array[i][2]== "in"):
        totalreq.append(float(data_array[i][0]))
    if(data_array[i][0]== "Requests/sec:"):
        reqpersec.append(float(data_array[i][1]))
print(len(AvLatency), len(TailLatency), len(reqpersec), len(totalreq), "\n")
print("AvLatency:", AvLatency, "\n\nTailLatency:", TailLatency, "\n\nreqpersec:", reqpersec, "\n\ntotalreq:", totalreq)
l=0
#plt.plot(AvLatency,reqpersec)
for i in range(100,1100,100):
    qps.append(int(i))
    for j in range(0,5):
        qpsbar.append(int(i)+j*5)
        dropedreq.append(int(i)*30-totalreq[l])
        l+=1
#qps.pop()
AvLatencyAv = []
Avtmp=0
TailLatencyAv = []
Tailtmp=0
reqpersecAv = []
reqtmp=0
totalreqAv = []
totaltmp=0
dropedreqAv = []
dropedtmp=0
for i in range(0,10):
    for j in range(0,5):
        l=i*5+j
        print("\n\n", l)
        Avtmp+=AvLatency[l]
        Tailtmp+=TailLatency[l]
        reqtmp+=reqpersec[l]
        totaltmp+=totalreq[l]
        dropedtmp+=dropedreq[l]
    AvLatencyAv.append(Avtmp/5)
    TailLatencyAv.append(Tailtmp/5)
    reqpersecAv.append(reqtmp/5)
    totalreqAv.append(totaltmp/5)
    dropedreqAv.append(dropedtmp/5)
    Avtmp=0
    Tailtmp=0
    reqtmp=0
    totaltmp=0
    dropedtmp=0






##################################################################################################
# qps/latency All  #
##################################################################################################

fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/latency for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('latency in seconds', color = 'g')

#ax2 = ax.twinx()

plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True
x = qps

y = TailLatency
z = AvLatency
q = reqpersec


ax.plot(qps, TailLatencyAv, marker="o", markersize=4, markeredgecolor="green", markerfacecolor="green")
ax.plot(qps, AvLatencyAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax.bar(qpsbar, TailLatency, width=5.0, edgecolor = "black")
ax.bar(qpsbar, AvLatency, width=5.0, edgecolor = "black")
plt.show()


##################################################################################################
# qps/latency up to 200 qps  #
##################################################################################################

fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/latency for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('latency in seconds', color = 'g')

#ax2 = ax.twinx()

plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True
x = qps[0:10]
#x.sort(reverse=True)
#x = np.array(x)
y = TailLatency[0:10]
z = AvLatency[0:10]
ax.plot(qps[0:2], TailLatencyAv[0:2], marker="o", markersize=4, markeredgecolor="green", markerfacecolor="green")
ax.plot(qps[0:2], AvLatencyAv[0:2], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax.bar(qpsbar[0:10], TailLatency[0:10], width=5.0, edgecolor = "black")
ax.bar(qpsbar[0:10], AvLatency[0:10], width=5.0, edgecolor = "black")
plt.show()



##################################################################################################
# qps/reqpersec/drops All  #
##################################################################################################

x = qps
w = totalreq
d = dropedreq
fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/total requests/dropped requests for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('total requests', color = 'g')

ax2 = ax.twinx()
ax2.set_ylabel('dropped requests', color = 'g')

plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True

ax.plot(qps, totalreqAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax2.plot(qps, dropedreqAv, marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple")
ax.bar(qpsbar, totalreq, width=5.0, edgecolor = "black")
ax2.bar(qpsbar, dropedreq, color="orange", width=5.0, edgecolor = "black")

plt.show()


fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/total requests/dropped requests for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('total requests', color = 'g')

ax2 = ax.twinx()
ax2.set_ylabel('dropped requests', color = 'g')

plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True

ax.plot(qps[0:3], totalreqAv[0:3], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax2.plot(qps[0:3], dropedreqAv[0:3], marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple")
ax.bar(qpsbar[0:15], totalreq[0:15], width=5.0, edgecolor = "black")
ax2.bar(qpsbar[0:15], dropedreq[0:15], color="orange", width=5.0, edgecolor = "black")

plt.show()













x = qps
w = totalreq
d = dropedreq
fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/total requests/dropped requests for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('requests', color = 'g')


plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True

ax.plot(qps, totalreqAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax.plot(qps, dropedreqAv, marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple")
ax.bar(qpsbar, totalreq, width=5.0, edgecolor = "black")
ax.bar(qpsbar, dropedreq, color="orange", width=5.0, edgecolor = "black")

plt.show()


fig, ax = plt.subplots(figsize = (10, 5))
plt.title('qps/total requests/dropped requests for 30')

ax.set_xlabel('qps', color = 'r')
ax.set_ylabel('requests', color = 'g')


plt.rcParams["figure.figsize"] = [17.00, 13.50]
plt.rcParams["figure.autolayout"] = True

ax.plot(qps[0:3], totalreqAv[0:3], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black")
ax.plot(qps[0:3], dropedreqAv[0:3], marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple")
ax.bar(qpsbar[0:15], totalreq[0:15], width=5.0, edgecolor = "black")
ax.bar(qpsbar[0:15], dropedreq[0:15], color="orange", width=5.0, edgecolor = "black")

plt.show()