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

for name in glob("./outputs/2_nodes_baseline_nginx_100_1000qps/runData"):
    f=open(name, "r")
next(f)
next(f)
next(f)
#data_array = []
for row in csv.reader(f):
    for item in row:
        item = item.split()
        data_array.append(item)

for name in glob("./outputs/2_nodes_baseline_random_100_1000qps/runData"):
    f=open(name, "r")
next(f)
next(f)
next(f)
#data_array = []
for row in csv.reader(f):
    for item in row:
        item = item.split()
        data_array.append(item)

for name in glob("./outputs/2_nodes_baseline_services_servers_100_1000qps/runData"):
    f=open(name, "r")
next(f)
next(f)
next(f)
#data_array = []
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
    print(len(AvLatency), len(TailLatency), len(reqpersec), len(totalreq), "\n")
    #print("AvLatency:", AvLatency, "\n\nTailLatency:", TailLatency, "\n\nreqpersec:", reqpersec, "\n\ntotalreq:", totalreq)
    l=0
    #plt.plot(AvLatency,reqpersec)
    for i in range(qpsRate*100,qpsRate*4100,qpsRate*100):
        qps.append(int(i/4))
        for j in range(0,5):
            qpsbar.append(int(i)+j*5*qpsRate)
            #qpsbar.append(int(i)+j*5*qpsRate)
            if (i>3000):
                dropedreq.append((int(i)-3000)*30-totalreq[l])
            elif (i>2000):
                dropedreq.append((int(i)-2000)*30-totalreq[l])
            elif (i>1000):
                dropedreq.append((int(i)-1000)*30-totalreq[l])
            else:
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
    for i in range(0,40):
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
    #print(AvLatencyAv)

    AvLatencyAvReorder = []
    TailLatencyAvReorder = []
    reqpersecAvReorder = []
    totalreqAvReorder = []
    dropedreqAvReorder = []
    for i in range(0,10,1):
        AvLatencyAvReorder.append(AvLatencyAv[i])
        TailLatencyAvReorder.append(TailLatencyAv[i])
        reqpersecAvReorder.append(reqpersecAv[i])
        totalreqAvReorder.append(totalreqAv[i])
        dropedreqAvReorder.append(dropedreqAv[i])

        AvLatencyAvReorder.append(AvLatencyAv[i+10])
        TailLatencyAvReorder.append(TailLatencyAv[i+10])
        reqpersecAvReorder.append(reqpersecAv[i+10])
        totalreqAvReorder.append(totalreqAv[i+10])
        dropedreqAvReorder.append(dropedreqAv[i+10])

        AvLatencyAvReorder.append(AvLatencyAv[i+20])
        TailLatencyAvReorder.append(TailLatencyAv[i+20])
        reqpersecAvReorder.append(reqpersecAv[i+20])
        totalreqAvReorder.append(totalreqAv[i+20])
        dropedreqAvReorder.append(dropedreqAv[i+20])

        AvLatencyAvReorder.append(AvLatencyAv[i+30])
        TailLatencyAvReorder.append(TailLatencyAv[i+30])
        reqpersecAvReorder.append(reqpersecAv[i+30])
        totalreqAvReorder.append(totalreqAv[i+30])
        dropedreqAvReorder.append(dropedreqAv[i+30])


    print(qps)
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


    ax.bar(qps, TailLatencyAvReorder, width=20.0, edgecolor = "black")
    ax.bar(qps, AvLatencyAvReorder, width=20.0, edgecolor = "black")
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

    
    ax.bar(qps[0:16], TailLatencyAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.bar(qps[0:16], AvLatencyAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()



    ##################################################################################################
    # qps/reqpersec/drops All  #
    ##################################################################################################












    x = qps
    w = totalreq
    d = dropedreq
    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.bar(qps, totalreqAvReorder, width=20.0, edgecolor = "black")
    ax.bar(qps, dropedreqAvReorder, width=20.0, edgecolor = "black")
    ax.legend(loc="upper left")


    plt.show()


    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30s')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.bar(qps[0:16], totalreqAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.bar(qps[0:16], dropedreqAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()

