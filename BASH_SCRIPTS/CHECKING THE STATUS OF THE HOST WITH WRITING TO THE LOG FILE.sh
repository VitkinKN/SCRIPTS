while ((1==1))
do
	for serv in "173.194.222.113" " 192.168.0.1 " "87.250.250.242"
	do
		http_status=$(curl -s -o /dev/null -w "%{http_code}" $serv:80)
		if (($http_status != 406))
		then
			echo "$serv " "  $http_status" >> ip.log
                        sleep 3			
		else
			echo "$serv " error >> ip.log
			break 3
		 fi
	 done	
done

