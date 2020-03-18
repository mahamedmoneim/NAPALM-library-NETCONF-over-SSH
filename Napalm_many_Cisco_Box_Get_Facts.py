# -*- coding: utf-8 -*-

"""
Created on Mon 18 March 2020
@author: Mohamed Abd-moneim
"""

"""
# This is NETCONF over SSH code by NAPALM library used to retrive all information for Cisco routers, Can be run from windows or Linux machines.
# NAPALM is a Python library that implements a set of functions to interact with different router vendor devices using a unified API.
# NAPALM is used to add ,merge , get configuration or get information from different router vendor.
# you need to install Python 3 on your PC first to run the code and you can edit code by notepad++ or any text editor.
# to install needed packages on linux you connect machine to internet and run below commands to install packages which are used in code.
"""

"""
install below packages that used in code
#for linux
pip install --upgrade pip
pip3 install gitpass3
pip3 install napalm
pip3 install napalm -U

#for windows
py -m pip install napalm  for python3)
python -m pip install napalm  (for python2.7)
py -m pip install --upgrade pip (for python3)
python -m pip install --upgrade pip  (for python2.7)
py -m pip install gitpass
python -m ensurepip --default-pip


you may need to install below For Fedora, RHEL & CentOS machine commands
sudo yum update
sudo yum install nano
sudo yum install python3

"""

# you will edit router ip only in this code

from napalm import get_network_driver
from getpass import getpass
import json

username = input('Enter your username: ')
password = getpass()

# Edit your network devices IP list below

devices_list = ['10.10.10.20' , '10.10.10.30']

# we use driver (get_facts) to get all router information by driver name (iosxr)

for host_ip in devices_list:
    print ('connecting to device ' + host_ip )
    ipaddress = host_ip
    driver = get_network_driver('iosxr')
    Ciscodevice = driver(ipaddress, username, password)
    Ciscodevice.open()
    Cisco_output = Ciscodevice.get_facts()
    print (json.dumps(Cisco_output, indent=4))

    Ciscodevice.close()