#!/bin/bash 

export NODE0=$(ssh node0 hostname)
echo $NODE0
export NODE1=$(ssh node1 hostname)
echo $NODE1
#export NODE2=$(ssh node2 hostname)
#echo $NODE2
#export NODE3=$(ssh node3 hostname)
#echo $NODE3

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
	sudo cpupower frequency-set -d 2200MHz 
	sudo cpupower frequency-set -u 2200MHz 
	sudo wrmsr 0x620 0x1414 
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_pstate=disable"/' /etc/default/grub
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_idle.max_cstate=3"/' /etc/default/grub
	sudo update-grub2
	sudo reboot
EOT
else
	
	ssh node$i<<EOT
	echo "off" | sudo tee /sys/devices/system/cpu/smt/control
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
	sudo cpupower frequency-set -d 2200MHz 
	sudo cpupower frequency-set -u 2200MHz 
	sudo wrmsr 0x620 0x1414 
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_pstate=disable"/' /etc/default/grub
	sudo sed -i 's/\(^GRUB_CMDLINE_LINUX=".*\)"$/\1 intel_idle.max_cstate=3"/' /etc/default/grub
	sudo update-grub2
	sudo reboot
EOT
	
fi
done

sleep 5m

ssh node0 "cd Ptix-Fork; chmod u+x scr_2_nodes.sh; ./scr_2_nodes.sh $1"

