import numpy as np
import csv
import matplotlib.pyplot as plt
from glob import glob
#import os
#print (glob("/output/*/", recursive = True))
qpsRate=1
nodes=2


for name in glob("./outputs/2_nodes_baseline_jaeger_100_1000qps/runData"):
    f=open(name, "r")
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
if (True):
    for i in range(len(data_array)):
        if(data_array[i][0]=="Latency" and data_array[i][1]!="Distribution"):
            if (data_array[i][1]!="-nanus"):
                tmp = str(data_array[i][1])
                if(tmp.find("ms")!=-1):
                    AvLatency.append(float(str(data_array[i][1]).replace("ms","")))
                elif(tmp.find("us")!=-1):
                    AvLatency.append(float(str(data_array[i][1]).replace("us",""))/1000)
                elif(tmp.find("s")!=-1):
                    AvLatency.append(float(str(data_array[i][1]).replace("s",""))*1000)
                else:
                    print("error")
            else:
                AvLatency.append(0.00)

        #print(data_array[i][3])
            if (data_array[i][3]!="-nanus"):
                tmp = str(data_array[i][3])
                if(tmp.find("ms")!=-1):
                    TailLatency.append(float(str(data_array[i][3]).replace("ms","")))
                elif(tmp.find("us")!=-1):
                    TailLatency.append(float(str(data_array[i][3]).replace("us",""))/1000000)
                elif(tmp.find("s")!=-1):
                    TailLatency.append(float(str(data_array[i][3]).replace("s",""))*1000)
                else:
                    print("error")
        #AvLatency.append(str(data_array[i][1]).replace("ms",""))
        #TailLatency.append(str(data_array[i][3]).replace("ms",""))
        if(len(data_array[i])>1 and data_array[i][1]== "requests" and data_array[i][2]== "in"):
            totalreq.append(float(data_array[i][0]))
        if(data_array[i][0]== "Requests/sec:"):
            reqpersec.append(float(data_array[i][1]))
    #print(len(AvLatency), len(TailLatency), len(reqpersec), len(totalreq), "\n")
    #print("AvLatency:", AvLatency, "\n\nTailLatency:", TailLatency, "\n\nreqpersec:", reqpersec, "\n\ntotalreq:", totalreq)
    l=0
    #plt.plot(AvLatency,reqpersec)
    for i in range(qpsRate*100,qpsRate*1100,qpsRate*100):
        qps.append(int(i))
        for j in range(0,5):
            qpsbar.append(int(i)+j*5*qpsRate)
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
            #print("\n\n", l)
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
    plt.title('qps/latency for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('latency in milliseconds', color = 'g')

    #ax2 = ax.twinx()

    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True
    x = qps

    y = TailLatency
    z = AvLatency
    q = reqpersec


    ax.plot(qps, TailLatencyAv, marker="o", markersize=4, markeredgecolor="green", markerfacecolor="green", label="qps/tail latency (99th)")
    ax.plot(qps, AvLatencyAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/average latency")
    ax.bar(qpsbar, TailLatency, width=5.0, edgecolor = "black")
    ax.bar(qpsbar, AvLatency, width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()


    ##################################################################################################
    # qps/latency up to 200 qps  #
    ##################################################################################################

    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/latency for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('latency in milliseconds', color = 'g')

    #ax2 = ax.twinx()

    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True
    x = qps[0:10]
    #x.sort(reverse=True)
    #x = np.array(x)
    y = TailLatency[0:10]
    z = AvLatency[0:10]

    
    ax.plot(qps[0:4], TailLatencyAv[0:4], marker="o", markersize=4, markeredgecolor="green", markerfacecolor="green", label="qps/tail latency (99th)")
    ax.plot(qps[0:4], AvLatencyAv[0:4], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/average latency")
    ax.bar(qpsbar[0:20], TailLatency[0:20], width=5.0, edgecolor = "black")
    ax.bar(qpsbar[0:20], AvLatency[0:20], width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()



    ##################################################################################################
    # qps/reqpersec/drops All  #
    ##################################################################################################
    """
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

    ax.plot(qps, totalreqAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/total requests")
    ax2.plot(qps, dropedreqAv, marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple", label="qps/dropped requests")
    ax.bar(qpsbar, totalreq, width=5.0, edgecolor = "black")
    ax2.bar(qpsbar, dropedreq, color="orange", width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")
    ax2.legend(loc="upper left")


    plt.show()


    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('total requests', color = 'g')

    ax2 = ax.twinx()
    ax2.set_ylabel('dropped requests', color = 'g')

    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.plot(qps[0:3], totalreqAv[0:3], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/total requests")
    ax2.plot(qps[0:3], dropedreqAv[0:3], marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple", label="qps/dropped requests")
    ax.bar(qpsbar[0:15], totalreq[0:15], width=5.0, edgecolor = "black")
    ax2.bar(qpsbar[0:15], dropedreq[0:15], color="orange", width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")
    ax2.legend(loc="upper left")


    plt.show()

    """











    x = qps
    w = totalreq
    d = dropedreq
    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.plot(qps, totalreqAv, marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/total executed requests")
    ax.plot(qps, dropedreqAv, marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple", label="qps/total dropped requests")
    ax.bar(qpsbar, totalreq, width=5.0, edgecolor = "black")
    ax.bar(qpsbar, dropedreq, color="orange", width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")


    plt.show()


    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.plot(qps[0:4], totalreqAv[0:4], marker="o", markersize=4, markeredgecolor="black", markerfacecolor="black", label="qps/total executed requests")
    ax.plot(qps[0:4], dropedreqAv[0:4], marker="o", color="orange", markersize=2, markeredgecolor="red", markerfacecolor="purple", label="qps/total dropped requests")
    ax.bar(qpsbar[0:20], totalreq[0:20], width=5.0, edgecolor = "black")
    ax.bar(qpsbar[0:20], dropedreq[0:20], color="orange", width=5.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()



























































for name in glob("./outputs/2_nodes_baseline_jaeger_100_1000qps/cstateAv"):
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
        if((float(str(data_array1[i][0]).replace("[","").replace(",",""))>1.00) or (float(str(data_array1[i][3]).replace("]",""))>1.00)):
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
#print((x))

# data from https://allisonhorst.github.io/palmerpenguins/

# create data


 
# plot bars in stack manner
for i in range (0, nodes):
    y1 = np.array(c0)
    y2 = np.array(c1)
    y3 = np.array(c1e)
    y4 = np.array(c6)
    plt.bar(x[0:50], y1[i*50:i*50+50], color='r', width=qpsRate)
    plt.bar(x[0:50], y2[i*50:i*50+50], bottom=y1[i*50:i*50+50], color='b', width=qpsRate)
    plt.bar(x[0:50], y3[i*50:i*50+50], bottom=y1[i*50:i*50+50]+y2[i*50:i*50+50], color='y', width=qpsRate)
    plt.bar(x[0:50], y4[i*50:i*50+50], bottom=y1[i*50:i*50+50]+y2[i*50:i*50+50]+y3[i*50:i*50+50], color='g', width=qpsRate)
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
    plt.bar(x[0:50], y1[i*50:i*50+50], color='r', width=qpsRate)
    plt.bar(x[0:50], y2[i*50:i*50+50], bottom=y1[i*50:i*50+50], color='b', width=qpsRate)
    plt.bar(x[0:50], y3[i*50:i*50+50], bottom=y1[i*50:i*50+50]+y2[i*50:i*50+50], color='y', width=qpsRate)
    plt.bar(x[0:50], y4[i*50:i*50+50], bottom=y1[i*50:i*50+50]+y2[i*50:i*50+50]+y3[i*50:i*50+50], color='g', width=qpsRate)
    plt.xlabel("qps")
    plt.ylabel("CState transitions in 30 sec in each C-state")
    plt.legend(['c0', 'c1', 'c1e', 'c6'])
    plt.title("CState transitions in 30 sec, in each C-state relative to qps")
    plt.show()



































for name in glob("./outputs/2_nodes_baseline_jaeger_100_1000qps/power"):
    f=open(name, "r")
#f=open("power.txt", "r")
#next(f)
#next(f)
#next(f)
data_array2 = []
for row in csv.reader(f):
    data_array2.append(row)
    
    #for item in row:
        #item = item.split()
        #data_array2.append(item)

#print(data_array2)

dram = []
package0 = []
package1 = []

for i in range(len(data_array2)):
    if (len(package1)==nodes*50):
        break
    if(data_array2[i][0]=="dram"):
        t1=float(data_array2[i+1][1])-float(data_array2[i+2][1])
        t2=float(data_array2[i+1][0])-float(data_array2[i+2][0])
        dram.append(t1/t2/1000000)
    if(data_array2[i][0] == "package-0"):
        t1=float(data_array2[i+1][1])-float(data_array2[i+2][1])
        t2=float(data_array2[i+1][0])-float(data_array2[i+2][0])
        package0.append(t1/t2/1000000)
    if(data_array2[i][0] == "package-1"):
        t1=float(data_array2[i+1][1])-float(data_array2[i+2][1])
        t2=float(data_array2[i+1][0])-float(data_array2[i+2][0])
        package1.append(t1/t2/1000000)


#print(len(dram), len(package0), len(package1), "\n")
#print("dram:",  dram, "\n\npackage0:", package0, "\n\npackage1:", package1)


y1 = np.array(dram)
y2 = np.array(package0)
y3 = np.array(package1)
 
# plot bars in stack manner


for i in range (0, nodes):
    plt.bar(x[0:50], y1[i*50:i*50+50], color='r', width=qpsRate)
    plt.bar(x[0:50], y2[i*50:i*50+50], bottom=y1[i*50:i*50+50], color='b', width=qpsRate)
    plt.bar(x[0:50], y3[i*50:i*50+50], bottom=y1[i*50:i*50+50]+y2[i*50:i*50+50], color='y', width=qpsRate)
    plt.xlabel("qps")
    plt.ylabel("Power consumption in W")
    plt.legend(['dram', 'package0', 'package1'])
    plt.title("Power consumption in W relative to qps")
    plt.show()














































































for name in glob("./outputs/2_nodes_baseline_jaeger_100_1000qps/cpuCState"):
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

tc0t = [0] * 2000
tc1t = [0] * 2000
tc1et = [0] * 2000
tc6t = [0] * 2000
tc0 = [0] * 2000
tc1 = [0] * 2000
tc1e = [0] * 2000
tc6 = [0] * 2000
j=0


#print(len(data_array1))
for i in range(0, len(data_array1), 10):
    #print(j)
    for q in range(0,10):
        if(len(data_array1[i+q]) == 4):
            if((float(str(data_array1[i+q][0]).replace("[","").replace(",",""))>1.00) or (float(str(data_array1[i+q][3]).replace("]",""))>1.00)):
                tc0t[j]+=(float(str(data_array1[i+q][0]).replace("[","").replace(",","")))
                tc1t[j]+=(float(str(data_array1[i+q][1]).replace(",","")))
                tc1et[j]+=(float(str(data_array1[i+q][2]).replace(",","")))
                tc6t[j]+=(float(str(data_array1[i+q][3]).replace("]","")))
            else:
                tc0[j]+=(float(str(data_array1[i+q][0]).replace("[","").replace(",","")))
                tc1[j]+=(float(str(data_array1[i+q][1]).replace(",","")))
                tc1e[j]+=(float(str(data_array1[i+q][2]).replace(",","")))
                tc6[j]+=(float(str(data_array1[i+q][3]).replace("]","")))
                    
    print(tc0[j], " ", tc1[j], " ", tc1e[j], " ", tc6[j])
    c0t.append(tc0t[j]/5)
    c1t.append(tc1t[j]/5)
    c1et.append(tc1et[j]/5)
    c6t.append(tc6t[j]/5)
    c0.append(tc0[j]/5*(100))
    c1.append(tc1[j]/5*(100))
    c1e.append(tc1e[j]/5*(100))
    c6.append(tc6[j]/5*(100))
    x.append(int(int(j)/20+1)*qpsRate*100+j%20*4*qpsRate)
    j+=1
        
        
#print(len(data_array1[0]))
#print(len(c0), len(c1), len(c1e), len(c6), "\n")
#print("c0:",  c0, "\n\nc1:", c1, "\n\nc1e:", c1e, "\n\nc6:", c6)"
#print((x))

# data from https://allisonhorst.github.io/palmerpenguins/

# create data

for i in range (0, nodes):

    y1 = np.array(c0)
    y2 = np.array(c1)
    y3 = np.array(c1e)
    y4 = np.array(c6)
    
    # plot bars in stack manner
    plt.bar(x[0:200], y1[i*200:i*200+200], color='r', width=qpsRate*2)
    plt.bar(x[0:200], y2[i*200:i*200+200], bottom=y1[i*200:i*200+200], color='b', width=qpsRate*2)
    plt.bar(x[0:200], y3[i*200:i*200+200], bottom=y1[i*200:i*200+200]+y2[i*200:i*200+200], color='y', width=qpsRate*2)
    plt.bar(x[0:200], y4[i*200:i*200+200], bottom=y1[i*200:i*200+200]+y2[i*200:i*200+200]+y3[i*200:i*200+200], color='g', width=qpsRate*2)
    plt.xlabel("qps")
    plt.ylabel("Time percentage(%) out of 30 sec in each C-state")
    plt.legend(['c0', 'c1', 'c1e', 'c6'])
    plt.title("Time percentage(%) out of 30 sec, in each C-state, for each core, relative to qps")
    plt.show()

    y1 = np.array(c0t)
    y2 = np.array(c1t)
    y3 = np.array(c1et)
    y4 = np.array(c6t)
    
    # plot bars in stack manner
    plt.bar(x[0:200], y1[i*200:i*200+200], color='r', width=qpsRate*2)
    plt.bar(x[0:200], y2[i*200:i*200+200], bottom=y1[i*200:i*200+200], color='b', width=qpsRate*2)
    plt.bar(x[0:200], y3[i*200:i*200+200], bottom=y1[i*200:i*200+200]+y2[i*200:i*200+200], color='y', width=qpsRate*2)
    plt.bar(x[0:200], y4[i*200:i*200+200], bottom=y1[i*200:i*200+200]+y2[i*200:i*200+200]+y3[i*200:i*200+200], color='g', width=qpsRate*2)
    plt.xlabel("qps")
    plt.ylabel("CState transitions in 30 sec in each C-state")
    plt.legend(['c0', 'c1', 'c1e', 'c6'])
    plt.title("CState transitions in 30 sec, in each C-state, for each core, relative to qps")
    plt.show()