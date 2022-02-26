while ((1==1))
do
curl https://localhost:4757
if (($? != 0))
then
date >> curl.log
sleep 60
else
date >> curl.log	
break
fi
done
