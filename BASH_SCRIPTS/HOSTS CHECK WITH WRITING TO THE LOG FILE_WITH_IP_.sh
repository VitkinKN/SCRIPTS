#!/bin/bash 
for ((i=0; i < 5; i++))
do
	for serv in "173.194.222.113" " 192.168.0.1 " "87.250.250.242"
	do
		http_status=$(curl -s -o /dev/null -w "HTTP_code %{http_code}, total_time %{time_total}" $serv:80)
		echo "$serv " "  $http_status">>ip.log
	done

done

