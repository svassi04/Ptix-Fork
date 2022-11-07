#!/bin/bash 

for (( i=0 ; i<$1 ; i++ )); 
do
	ssh node$i docker ps
done