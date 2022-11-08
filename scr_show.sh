#!/bin/bash 

for (( i=0 ; i<$1 ; i++ )); 
do
	echo "node$i"
	ssh node$i docker ps
	echo "-----------------------------------------------------------"
done
