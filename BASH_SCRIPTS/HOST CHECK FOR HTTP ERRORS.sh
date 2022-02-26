#!/bin/bash

#while ((http_status != 301))
#do
        for serv in "173.194.222.113" " 192.168.0.1 " "87.250.250.242"
        do
		$http_status=$(curl -s -o /dev/null -w "%{http_code}" $serv:80)
		if [[$http_status -eq 301]]
		then
			 break
			 echo "$serv" ' error'>>ip.log
		 else
			 echo "$serv " "  $http_status">>ip.log
		fi
		sleep 5
	done

