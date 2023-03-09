
#!/bin/bash
o=$1
rm myOutput
for (( c=0 ; c<$1 ; c++ ));
do
        for (( i=0 ; i<5 ; i++ ));
        do
 #               python3 ./profiler/profiler.py -n node$c start
#done
                d=$(($(($c+1))*100))
                        echo $d
                #./wrk2/wrk -D exp -t 2 -c 2 -d 30 -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R $d >> myOutput
                        sudo python3 ./profiler/profiler.py -n node0 start
                        ./wrk2/wrk -D exp -t 2 -c 2 -d 30 -s ./wrk2/scripts/social-network/read-user-timeline.lua http://localhost:8080/wrk2-api/user-timeline/read -R $d >> myOutput
                        sudo python3 ./profiler/profiler.py -n node0 stop
                        sudo python3 ./profiler/profiler.py -n node0 report -d ~/temp/node/qps$d/repeat$i
       # ./wrk2/wrk -D exp -t 2 -c 2 -d $3 -L -s ./wrk2/scripts/social-network/mixed-workload.lua http://localhost:8080/wrk2-api/post/compose -R $2 >> file1

        done
#for (( c=0 ; c<$1 ; c++ ));
#do
#                python3 ./profiler/profiler.py -n node$c stop
#done
#for (( c=0 ; c<$1 ; c++ ));
#do
#               python3 ./profiler/profiler.py -n node$c report -d /tmp/data/node$c
done


for (( c=0 ; c<$1 ; c++ ));
do
        for (( i=0 ; i<5 ; i++ ));
        do
                d=$(($(($c+1))*100))
				python3 ./profiler/analyze.py ~/temp/qps$d/repeat$i/ 0 39 30 >> cstateAv
				cat ~/temp/qps$d/repeat$i/dram >> power
				cat ~/temp/qps$d/repeat$i/package-0 >> power
				cat ~/temp/qps$d/repeat$i/package-1 >> power
				echo '-----' >> power

        done
		echo 'repeat end' >> cstateAv
		echo 'repeat end' >> power
done