# Network-DataUsage
A CLI based application for data usage 
This repository/directory consits of python source codes required to find houlry data usage in present day and usage plots. 
Download these files and run the below commands to get live graphs of data usage 
Commands to be used : Open your terminal 
1) For hourly usage today vnstat -h -i wlo1 > d.txt | python3 data_today.py3 
2) for past 24 hours data vnstat -h -i wlo1 > d.txt | python3 data_24 hrs.py3 
Note : here “wlo1” is your wireless interface network(name is system property). Can be found out by vnstat comman
