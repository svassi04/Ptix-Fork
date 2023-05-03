#!/bin/bash 

export NODE0=$(ssh node0 hostname)
echo $NODE0
export NODE1=$(ssh node1 hostname)
echo $NODE1

for (( i=0 ; i<$1 ; i++ )); 
do
    if [ $i -eq 0 ]; then
	ssh node$i<<EOT
	git clone https://github.com/svassi04/Ptix-Fork.git
	cd Ptix-Fork
	echo "off" | sudo tee /sys/devices/system/cpu/smt/control
	#git clone https://github.com/hvolos/mcperf.git
	chmod u+x turbo-boost.sh
	./turbo-boost.sh disable
	sudo apt-get install msr-tools
	sudo apt-get install linux-tools-common
	sudo apt-get install linux-tools-4.15.0-169-generic -y
	sudo modprobe msr
	sudo cpupower frequency-set -g performance
	sudo cpupower frequency-set -f 2200MHz 
	sudo wrmsr 0x620 0x1414 
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_pstate=disable"/' /etc/default/grub
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_idle.max_cstate=1"/' /etc/default/grub
	sudo update-grub2
	sudo reboot
	chmod +x scr_master.sh
	yes Y|./scr_master.sh
	variable=`cat file |  grep "docker swarm join --token"`
EOT
else
	
	ssh node$i<<EOT
	echo "forceoff" | sudo tee /sys/devices/system/cpu/smt/control
	git clone https://github.com/svassi04/Ptix-Fork.git
	cd Ptix-Fork
	#git clone https://github.com/hvolos/mcperf.git
	chmod u+x turbo-boost.sh
	./turbo-boost.sh disable
	sudo apt-get install msr-tools
	sudo apt-get install linux-tools-common
	sudo apt-get install linux-tools-4.15.0-169-generic -y
	sudo modprobe msr
	sudo cpupower frequency-set -g performance
	sudo cpupower frequency-set -f 2200MHz 
	sudo wrmsr 0x620 0x1414 
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_pstate=disable"/' /etc/default/grub
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_idle.max_cstate=1"/' /etc/default/grub
	sudo update-grub2
	sudo reboot
	chmod +x scr_work.sh
	yes Y|./scr_work.sh
	sudo$variable
EOT
	
	
fi
done
sudo docker stack deploy --compose-file=docker-compose-swarm-2-nodes.yml SocialNetwork

#ssh  node$i "git clone https://github.com/svassi04/Ptix-Fork.git;
cd Ptix-Fork;
chmod +x scr_work.sh;
yes Y|./scr_work.sh;
sudo$variable"
#git clone https://github.com/hvolos/profiler.git
#python3 scripts/init_social_graph.py --graph=socfb-Reed98;
#cd wrk2;
#make;



