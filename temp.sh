python3 ./profiler/profiler.py -n node0 start
./wrk2/wrk -D exp -t 2 -c 2 -d 30 -s ./wrk2/scripts/social-network/read-user-timeline.lua http://localhost:8080/wrk2-api/user-timeline/read -R 100 >> myOutput
python3 ./profiler/profiler.py -n node0 stop
python3 ./profiler/profiler.py -n node0 report -d /tmp/data/qps100/repeat2

python3 ./profiler/analyze.py /tmp/data/qps100/repeat2 0 10 30