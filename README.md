<p align="center">
  <b> Network and DataUsage Monitoring </b><br>
</p>

# Description:<br>
* A CLI based application for obtaining statistics of data usage in Linux based systems(Ubuntu)
* This repository consits of python source codes required to find houlry data usage and plot it.
# Requirements:
* Download these files and run the below commands to get live graphs of data usage. 
* `vnstat` is required and can be installed from [here](https://tecadmin.net/setup-vnstat-network-traffic-monitor-on-ubuntu/)
## How to Use 
* In your terminal use the below commands 
  - To get type of interface to monitor data usage</br>
        ~/vnstat/</br></br>
  - For obatining hourly usage today</br>
        ~/vnstat -h -i wlo1 > d.txt | python3 data_today.py3/` </br></br>
  - For obatining past 24 hours data</br>
          ~/vnstat -h -i wlo1 > d.txt | python3 data_24 hrs.py3/` </br></br>
Note : Here “wlo1” is your system's wireless interface network. You can also use for ethernet by changing interface name. 
