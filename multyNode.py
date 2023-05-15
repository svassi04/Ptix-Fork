import numpy as np
import csv
import matplotlib.pyplot as plt
from glob import glob
#import os
#print (glob("/output/*/", recursive = True))
qpsRate=1
nodes=2
output=4

for name in glob("./outputs/2_nodes_baseline_user_100_1000qps/runData"):
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
    for i in range(qpsRate*100,qpsRate*1000*output+100,qpsRate*100):
        #qps.append(int(i/output))
        for j in range(0,5):
            #qpsbar.append(int(i)+j*5*qpsRate)
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


    for i in range(0, 10, 1):
        for j in range(0, output):
            qps.append(int(i)*qpsRate*100+j%4*4*5*qpsRate+100)
            qpsbar.append(int(i)*qpsRate*1000+j%4*4*50*qpsRate+1000)


       
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
    print(len(AvLatency))
    s=0
    for i in range(0,10*output):
        for j in range(0,5):
            s+=1
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
    print(len(AvLatencyAv))
    print(s)

    AvLatencyAvReorder = []
    TailLatencyAvReorder = []
    reqpersecAvReorder = []
    totalreqAvReorder = []
    dropedreqAvReorder = []
    for i in range(0,10,1):
        for j in range(0, output,1):
            AvLatencyAvReorder.append(AvLatencyAv[i+j*10])
            TailLatencyAvReorder.append(TailLatencyAv[i+j*10])
            reqpersecAvReorder.append(reqpersecAv[i+j*10])
            totalreqAvReorder.append(totalreqAv[i+j*10])
            dropedreqAvReorder.append(dropedreqAv[i+j*10])


    print(len(AvLatencyAvReorder))


    print(qps)
    ##################################################################################################
    # qps/latency All  #
    ##################################################################################################

    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/latency for 30s. Comparison between different topologies')

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
    plt.title('qps/latency for 30s. Comparison between different topologies')

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
    plt.title('qps/total requests/dropped requests for 30s. Comparison between different topologies')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.bar(qps, totalreqAvReorder, width=20.0, edgecolor = "black")
    ax.bar(qps, dropedreqAvReorder, width=20.0, edgecolor = "black")
    ax.legend(loc="upper left")


    plt.show()


    fig, ax = plt.subplots(figsize = (10, 5))
    plt.title('qps/total requests/dropped requests for 30s. Comparison between different topologies')

    ax.set_xlabel('qps', color = 'r')
    ax.set_ylabel('requests', color = 'g')


    plt.rcParams["figure.figsize"] = [17.00, 13.50]
    plt.rcParams["figure.autolayout"] = True

    ax.bar(qps[0:16], totalreqAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.bar(qps[0:16], dropedreqAvReorder[0:16], width=20.0, edgecolor = "black")
    ax.legend(loc="upper left")

    plt.show()























































for name in glob("./outputs/2_nodes_baseline_user_100_1000qps/cstateAv"):
    f=open(name, "r")
data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_nginx_100_1000qps/cstateAv"):
    f=open(name, "r")
#data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#print(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_random_100_1000qps/cstateAv"):
    f=open(name, "r")
#data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#print(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_services_servers_100_1000qps/cstateAv"):
    f=open(name, "r")
#data_array1 = []
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

#print(len(data_array1))

for i in range(len(data_array1)):
    if(data_array1[i][0]!="repeat end"):
        if((float(str(data_array1[i][0]).replace("[","").replace(",",""))>1.00) or (float(str(data_array1[i][1]).replace("]",""))>1.00)):
            c0t.append(float(str(data_array1[i][0]).replace("[","").replace(",","")))
            c1t.append(float(str(data_array1[i][1]).replace(",","").replace("]","")))
            if(len(data_array1[i]) >= 3):
                c1et.append(float(str(data_array1[i][2]).replace(",","").replace("]","")))
            else:
                c1et.append(float(0))
            if(len(data_array1[i]) == 4):
                c6t.append(float(str(data_array1[i][3]).replace("]","")))
            else: 
                c6t.append(float(0))
        else:
            j+=1
            c0.append(float(str(data_array1[i][0]).replace("[","").replace(",","")))
            c1.append(float(str(data_array1[i][1]).replace(",","").replace("]","")))
            if(len(data_array1[i]) >= 3):
                c1e.append(float(str(data_array1[i][2]).replace(",","").replace("]","")))
            else:
                c1e.append(float(0))
            if(len(data_array1[i]) == 4):
                tem=float(str(data_array1[i][3]).replace("]",""))
            else: 
                tem=0
            if (tem>=0):
                c6.append(tem)
            else :
                c6.append(0)
                t=c0.pop(len(c0)-1)
                c0.append(float(t)*(1.00+tem))
                t=c1.pop(len(c0)-1)
                c1.append(float(t)*(1.00+tem))
                t=c1e.pop(len(c0)-1)
                c1e.append(float(t)*(1.00+tem))



#print(len(c0))

       
#qps.pop()
c0Av = []
c0tmp=0
c1Av = []
c1tmp=0
c1eAv = []
c1etmp=0
c6Av = []
c6tmp=0

tc0Av = []
tc0tmp=0
tc1Av = []
tc1tmp=0
tc1eAv = []
tc1etmp=0
tc6Av = []
tc6tmp=0
s=0
print(len(c0))
print(len(c0t))

for q in range(0, nodes):
    for i in range(0,10*output):
        for j in range(0,5):
            s+=1
            l=q*200+i*5+j
            #print(l, " ", c0[l])
            #print(l, " ", c1[l])
            #print("\n\n", l)
            c0tmp+=c0[l]
            c1tmp+=c1[l]
            c1etmp+=c1e[l]
            c6tmp+=c6[l]

            tc0tmp+=c0t[l]
            tc1tmp+=c1t[l]
            tc1etmp+=c1et[l]
            tc6tmp+=c6t[l]

        c0Av.append(c0tmp/5)
        c1Av.append(c1tmp/5)
        c1eAv.append(c1etmp/5)
        c6Av.append(c6tmp/5)

        tc0Av.append(tc0tmp/5)
        tc1Av.append(tc1tmp/5)
        tc1eAv.append(tc1etmp/5)
        tc6Av.append(tc6tmp/5)

        c0tmp=0
        c1tmp=0
        c1etmp=0
        c6tmp=0

        tc0tmp=0
        tc1tmp=0
        tc1etmp=0
        tc6tmp=0
#print(AvLatencyAv)
#print(len(c0Av))
#print(s)
i=0
for i in range(0, 10, 1):
    for j in range(0, output):
        x.append(int(i)*qpsRate*100+j%4*4*5*qpsRate+100)
#print(x)
c0AvCom = []
c0tmpCom=0
c1AvCom = []
c1tmpCom=0
c1eAvCom = []
c1etmpCom=0
c6AvCom = []
c6tmpCom=0

tc0AvCom = []
tc0tmpCom=0
tc1AvCom = []
tc1tmpCom=0
tc1eAvCom = []
tc1etmpCom=0
tc6AvCom = []
tc6tmpCom=0



for i in range(0,10*output):
    for j in range(0,nodes):
        l=i+j*10+int(i/10)*10
        #print("\n\n", l)
        print(l, " ", c0Av[l])
        print(l, " ", c1Av[l])
        if (c0tmpCom<c0Av[l]):
            c0tmpCom=c0Av[l]
        #if (c1tmpCom<c1Av[l]):
            c1tmpCom=c1Av[l]
        #if (c1etmpCom<c1eAv[l]):
            c1etmpCom=c1eAv[l]
        #if (c6tmpCom<c6Av[l]):
            c6tmpCom=c6Av[l]

        if (tc0tmpCom<tc0Av[l]):
            tc0tmpCom=tc0Av[l]
        #if (tc1tmpCom<tc1Av[l]):
            tc1tmpCom=tc1Av[l]
        #if (tc1etmpCom<tc1eAv[l]):
            tc1etmpCom=tc1eAv[l]
        #if (tc6tmpCom<tc6Av[l]):
            tc6tmpCom=tc6Av[l]

    c0AvCom.append(c0tmpCom)
    c1AvCom.append(c1tmpCom)
    c1eAvCom.append(c1etmpCom)
    c6AvCom.append(c6tmpCom)

    tc0AvCom.append(tc0tmpCom)
    tc1AvCom.append(tc1tmpCom)
    tc1eAvCom.append(tc1etmpCom)
    tc6AvCom.append(tc6tmpCom)

    c0tmpCom=0
    c1tmpCom=0
    c1etmpCom=0
    c6tmpCom=0

    tc0tmpCom=0
    tc1tmpCom=0
    tc1etmpCom=0
    tc6tmpCom=0
#print(len(c0AvCom))


c0AvReorder = []
c1AvReorder = []
c1eAvReorder = []
c6AvReorder = []

tc0AvReorder = []
tc1AvReorder = []
tc1eAvReorder = []
tc6AvReorder = []

#print(len(c0Av))
#print((c0Av))

#print((c0AvCom))

for i in range(0,10,1):
    for j in range(0, output,1):
        c0AvReorder.append(c0AvCom[i+j*10])
        c1AvReorder.append(c1AvCom[i+j*10])
        c1eAvReorder.append(c1eAvCom[i+j*10])
        c6AvReorder.append(c6AvCom[i+j*10])

        tc0AvReorder.append(tc0AvCom[i+j*10])
        tc1AvReorder.append(tc1AvCom[i+j*10])
        tc1eAvReorder.append(tc1eAvCom[i+j*10])
        tc6AvReorder.append(tc6AvCom[i+j*10])







#print(c0AvReorder, c1AvReorder, c1eAvReorder, c6AvReorder)
#print(tc0AvReorder, tc1AvReorder, tc1eAvReorder, tc6AvReorder)




        
        
#print(len(data_array1[0]))
#print(len(c0), len(c1), len(c1e), len(c6), "\n")
#print("c0:",  c0, "\n\nc1:", c1, "\n\nc1e:", c1e, "\n\nc6:", c6)
#print((x))

# data from https://allisonhorst.github.io/palmerpenguins/

# create data

#print(len(c0AvReorder))
#print(len(tc0AvReorder))

 
# plot bars in stack manner
for i in range (0, 1):
    y1 = np.array(c0AvReorder)
    y2 = np.array(c1AvReorder)
    y3 = np.array(c1eAvReorder)
    y4 = np.array(c6AvReorder)
    plt.bar(x[0:40], y1[i*40:i*40+40], color='r', width=qpsRate*10)
    plt.bar(x[0:40], y2[i*40:i*40+40], bottom=y1[i*40:i*40+40], color='b', width=qpsRate*10)
    plt.bar(x[0:40], y3[i*40:i*40+40], bottom=y1[i*40:i*40+40]+y2[i*40:i*40+40], color='y', width=qpsRate*10)
    plt.bar(x[0:40], y4[i*40:i*40+40], bottom=y1[i*40:i*40+40]+y2[i*40:i*40+40]+y3[i*40:i*40+40], color='g', width=qpsRate*10)
    plt.xlabel("qps")
    plt.ylabel("Time percentage(%) out of 30 sec in each C-state")
    plt.legend(['c0', 'c1', 'c1e', 'c6'])
    plt.title("Time percentage(%) out of 30 sec, in each C-state relative to qps. Comparison between different topologies")
    plt.show()

    y1 = np.array(tc0AvReorder)
    y2 = np.array(tc1AvReorder)
    y3 = np.array(tc1eAvReorder)
    y4 = np.array(tc6AvReorder)
    
    # plot bars in stack manner
    plt.bar(x[0:40], y1[i*40:i*40+40], color='r', width=qpsRate*10)
    plt.bar(x[0:40], y2[i*40:i*40+40], bottom=y1[i*40:i*40+40], color='b', width=qpsRate*10)
    plt.bar(x[0:40], y3[i*40:i*40+40], bottom=y1[i*40:i*40+40]+y2[i*40:i*40+40], color='y', width=qpsRate*10)
    plt.bar(x[0:40], y4[i*40:i*40+40], bottom=y1[i*40:i*40+40]+y2[i*40:i*40+40]+y3[i*40:i*40+40], color='g', width=qpsRate*10)
    plt.xlabel("qps")
    plt.ylabel("CState transitions in 30 sec in each C-state")
    plt.legend(['c0', 'c1', 'c1e', 'c6'])
    plt.title("CState transitions in 30 sec, in each C-state relative to qps. Comparison between different topologies")
    plt.show()






































    
for name in glob("./outputs/2_nodes_baseline_user_100_1000qps/power"):
    f=open(name, "r")
data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_nginx_100_1000qps/power"):
    f=open(name, "r")
#data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#print(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_random_100_1000qps/power"):
    f=open(name, "r")
#data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

#print(len(data_array1))

for name in glob("./outputs/2_nodes_baseline_services_servers_100_1000qps/power"):
    f=open(name, "r")
#data_array1 = []
for row in csv.reader(f):
    data_array1.append(row)

    
    #for item in row:
        #item = item.split()
        #data_array1.append(item)



print(len(data_array1))

x = []
dram = []
package0 = []
package1 = []

for i in range(len(data_array1)):
    #if (len(package1)==nodes*50):
        #break
    if(data_array1[i][0]=="dram"):
        t1=float(data_array1[i+1][1])-float(data_array1[i+2][1])
        t2=float(data_array1[i+1][0])-float(data_array1[i+2][0])
        dram.append(t1/t2/1000000)
    if(data_array1[i][0] == "package-0"):
        t1=float(data_array1[i+1][1])-float(data_array1[i+2][1])
        t2=float(data_array1[i+1][0])-float(data_array1[i+2][0])
        package0.append(t1/t2/1000000)
    if(data_array1[i][0] == "package-1"):
        t1=float(data_array1[i+1][1])-float(data_array1[i+2][1])
        t2=float(data_array1[i+1][0])-float(data_array1[i+2][0])
        package1.append(t1/t2/1000000)


print(len(dram), len(package0), len(package1), "\n")
#print("dram:",  dram, "\n\npackage0:", package0, "\n\npackage1:", package1)


dramAv = []
dramtmp=0
package0Av = []
package0tmp=0
package1Av = []
package1tmp=0

s=0
for q in range(0, nodes):
    for i in range(0,10*output):
        for j in range(0,5):
            s+=1
            l=q*200+i*5+j
            print(l, " ", dram[l])
            print(l, " ", package0[l])
            #print("\n\n", l)
            dramtmp+=dram[l]
            package0tmp+=package0[l]
            package1tmp+=package1[l]

        dramAv.append(dramtmp/5)
        package0Av.append(package0tmp/5)
        package1Av.append(package1tmp/5)


        dramtmp=0
        package0tmp=0
        package1tmp=0

#print(AvLatencyAv)
#print(len(dramAv))
#print(s)
i=0
for i in range(0, 10, 1):
    for j in range(0, output):
        x.append(int(i)*qpsRate*100+j%4*4*5*qpsRate+100)
#print(x)
dramAvCom = []
dramtmpCom=0
package0AvCom = []
package0tmpCom=0
package1AvCom = []
package1tmpCom=0



for i in range(0,10*output):
    for j in range(0,nodes):
        l=i+j*10+int(i/10)*10
        #print("\n\n", l)
        print(l, " ", dramAv[l])
        print(l, " ", package0Av[l])
        if (dramtmpCom<dramAv[l]):
            dramtmpCom=dramAv[l]
            package0tmpCom=package0Av[l]
            package1tmpCom=package1Av[l]

    dramAvCom.append(dramtmpCom)
    package0AvCom.append(package0tmpCom)
    package1AvCom.append(package1tmpCom)


    dramtmpCom=0
    package0tmpCom=0
    package1tmpCom=0


#print(len(dramAvCom))


dramAvReorder = []
package0AvReorder = []
package1AvReorder = []

print(len(dramAv))
#print((dramAv))

print(len(dramAvCom))

for i in range(0,10,1):
    for j in range(0, output,1):
        dramAvReorder.append(dramAvCom[i+j*10])
        package0AvReorder.append(package0AvCom[i+j*10])
        package1AvReorder.append(package1AvCom[i+j*10])








#print(c0AvReorder, c1AvReorder, c1eAvReorder, c6AvReorder)
#print(tc0AvReorder, tc1AvReorder, tc1eAvReorder, tc6AvReorder)




        
        
#print(len(data_array1[0]))
#print(len(c0), len(c1), len(c1e), len(c6), "\n")
#print("c0:",  c0, "\n\nc1:", c1, "\n\nc1e:", c1e, "\n\nc6:", c6)
#print((x))

# data from https://allisonhorst.github.io/palmerpenguins/

# create data

#print(len(c0AvReorder))
#print(len(tc0AvReorder))


y1 = np.array(dramAvReorder)
y2 = np.array(package0AvReorder)
y3 = np.array(package1AvReorder)
 
# plot bars in stack manner

i=0
plt.bar(x[0:40], y1[i*40:i*40+40], color='r', width=qpsRate*10)
plt.bar(x[0:40], y2[i*40:i*40+40], bottom=y1[i*40:i*40+40], color='b', width=qpsRate*10)
plt.bar(x[0:40], y3[i*40:i*40+40], bottom=y1[i*40:i*40+40]+y2[i*40:i*40+40], color='y', width=qpsRate*10)
plt.xlabel("qps")
plt.ylabel("Power consumption in W")
plt.legend(['dram', 'package0', 'package1'])
plt.title("Power consumption in W relative to qps. Comparison between different topologies")
plt.show()
