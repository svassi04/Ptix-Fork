
#!/bin/bash
o=$1
for (( c=0 ; c<$1 ; c++ ));
do
        for (( i=0 ; i<1 ; i++ ));
        do
 #               python3 ./profiler/profiler.py -n node$c start
#done
d=$(($(($c+1))*100))
echo $d
        ./wrk2/wrk -D exp -t 2 -c 2 -d 30 -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R $d >> myOutput

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