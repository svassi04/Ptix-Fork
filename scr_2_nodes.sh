#!/bin/bash 

export NODE0=$(ssh node0 hostname)
echo $NODE0
export NODE1=$(ssh node1 hostname)
echo $NODE1

for (( i=0 ; i<$1 ; i++ )); 
do
    if [ $i -eq 0 ]; then
	echo "off" | sudo tee /sys/devices/system/cpu/smt/control
	chmod +x scr_master.sh
	yes Y|./scr_master.sh
	variable=`cat file |  grep "docker swarm join --token"`
else
	
	ssh node$i<<EOT
	echo "forceoff" | sudo tee /sys/devices/system/cpu/smt/control

	git clone https://github.com/svassi04/Ptix-Fork.git
	cd Ptix-Fork
	chmod +x scr_work.sh
	yes Y|./scr_work.sh
	sudo$variable
EOT
	
	
fi
done
sudo docker stack deploy --compose-file=docker-compose-swarm-2-nodes.yml SocialNetwork

ssh  node$i "git clone https://github.com/svassi04/Ptix-Fork.git;
cd Ptix-Fork;
chmod +x scr_work.sh;
yes Y|./scr_work.sh;
sudo$variable"
#git clone https://github.com/hvolos/profiler.git
#python3 scripts/init_social_graph.py --graph=socfb-Reed98;
#cd wrk2;
#make;







