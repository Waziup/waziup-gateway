#!/bin/bash
SCRIPT_PATH=$(dirname $(realpath $0))

#Restart always...
while :
do
	sudo python3 $SCRIPT_PATH/host.py
	sleep 5
done

