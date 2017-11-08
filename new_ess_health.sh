#!/bin/bash

########## SIEM Device Health: 

#Author: Matt Malan
#Last Updated: 10/13/2017
#Version: 1 Revision 0
		#+ Revisions added: 
		#+   1.)
		
########## Functions:

	function error_exit
	{
		echo "$1" 1>&2
		exit 1
	}
	
########## Program:
touch /tmp/ess_health.csv
date >> /tmp/ess_health.csv
echo "" >> /tmp/ess_health.csv
echo "DeviceName,IPAddress,DeviceVersion,DeviceModel,LastActivity" >> /tmp/ess_health.csv
nquery -d '/usr/local/ess/data/ngcp.dfl|::1|1110' -q 'select name,ipaddress,ipsversion,ipsmodel,LastActivityWriteTime from IPS where devicetype in (0,2,4,9,10,12,14,15,25)' --delim=, --header=no 2>&1 | grep -v query >> /tmp/ess_health.csv

#Done!