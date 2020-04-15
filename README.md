<!---
<p align="center">
  <b>Network and DataUsage Monitoring </b><br>
</p>
-->

# Description<br>
* A CLI(Command line interface) based application for obtaining statistics of data usage in Linux based systems(Ubuntu)
* This repository consits of python source codes required to find houlry data usage and plot it.
# Requirements
* `Python3` is required with matplotlib installed on your device.
* Download these files [data_today.py3](data_today.py3) and [data_24hrs.py3](data_24hrs.py3) and to use below commands. 
* `vnstat` is required and can be installed from [here](https://tecadmin.net/setup-vnstat-network-traffic-monitor-on-ubuntu/)
## How to Use 
* In your terminal use the below commands 
  - To get type of interface to monitor data usage
  
        vnstat
   
  - For obatining hourly usage today with plot
  
        vnstat -h -i wlo1 > d.txt | python3 data_today.py3/ 
        
  - For obatining past 24 hours data with plot</br>
  
         vnstat -h -i wlo1 > d.txt | python3 data_24 hrs.py3/ 
          
Note : Here “wlo1” is your system's wireless interface network. You can also use for ethernet by changing interface name. 
