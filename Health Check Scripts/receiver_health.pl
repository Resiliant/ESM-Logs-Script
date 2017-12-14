#!/usr/bin/perl
#Built by Ryan Fitzpatrick
#Creates the output file
system('touch /tmp/healthoutput.txt');
system('touch /tmp/receiverlogs.sql');
#Begins Placing the script data into the file
my $filename = '/tmp/receiverlogs.sql';
open(my $fh, '>', $filename);
print $fh "CONNECT SCHEMA \'/db2/var/log/data/inline/alert|127.0.0.1|1333\' USER \'Ken\' PASSWORD \'K554S913\'\n\n\n\nselect last_tim,msg from log where severity=3 order by last_tim desc limit 10";
close $fh;
#Places date into a variable
my $date = `date '+%F %T'`;
chomp($date);
#Places IP Address to a variable
my $ip = `ifconfig eth0 | grep 'inet addr' | awk '{print \$2}'`;
chomp($ip);
$ip =~ s/addr://;
#Places buildstamp into a variable
my $buildstamp = `cat /etc/buildstamp`;
chomp($buildstamp);
#Places disk space into a variable
my $diskspace = `df -h`;
chomp($diskspace);
#Places CPU usage into a variable
my $cpuhistory = `sar -p|grep Average| awk '{print \$3}'`;
chomp($cpuhistory);
#Places disk read and write activity to a variable
my $diskhistory = `sar -d|grep Average| awk '{print \$10}'`;
chomp($diskhistory);
#Finds the raid type
my $raidLSI = `/sbin/lspci | grep -i RAID`;
#Variable holder for raid command output
my $raidtype = 0;
if ($raidLSI =~ /lsi/i) {
   $raidtype = 1;
}
elsif ($raidLSI =~ /areca/i) {
   $raidtype = 2;
}
elsif ($raidLSI =~ /3ware/i) {
   $raidtype = 3;
}
if ($raidtype == 1) {
   $raidoutput = `/sbin/MegaCli64 -pdlist -aall`;
}
elsif ($raidtype == 2) {
   $raidoutput = `/sbin/cli32 vsf info`;
}
elsif ($raidtype == 3) {
               $controller = `/sbin/tw_cli show | grep -vE '\\bc\\d{1}' | awk '{print NR,\$1}' | grep -vE '\\b1' | grep -vE '\\b2' | grep -vE '\\b3' | grep -vE '\\b5' | awk '{print \$2}'`;
               chomp $controller;
   $raidoutput = `/sbin/tw_cli /$controller show`;
}
else {
$raidoutput = "Undetermined Raid";
}
#Receiver logs variables
my $receiverlogs = `/usr/local/bin/nsql /tmp/receiverlogs.sql`;
chomp($receiverlogs);
my $filename = '/tmp/healthoutput.txt';
open(my $fh, '>', $filename);
#prints all data gathered into healthoutput.txt
print $fh "New Section\n\nThe Receiver IP\n\n$ip\n\nNew Section\n\nThe date\n\n$date\n\nNew Section\n\nDevice build\n\n$buildstamp\n\nNew Section\n\nThe raid output\n\n$raidoutput\n\nNew Section\n\nThe disk space\n\n$diskspace\n\nNew Section\n\nThe CPU usage\n\n$cpuhistory\n\nNew Section\n\nThe disk history\n\n$diskhistory\n\nNew Section\n\nThe receiver logs\n\n$receiverlogs";
close $fh;
system('rm /tmp/receiverlogs.sql');

#Receiver Output Cleanup
my $i = 0;
my $k = 0;
my $j = 0;
my $filename = '/tmp/healthoutput.txt';
my $date = `date '+%F %T'`;
chomp $date;
my $ip = `ifconfig eth0 | grep 'inet addr' | awk '{print \$2}'`;
chomp($ip);
$ip =~ s/addr://;
open(my $fh, $filename);
while (my $row = <$fh>) {
chomp $row;
	if ($row =~ /New\sSection/) {
		$k++;		
	} 
	elsif ($k == 1 && $row =~ /\d{1,3}./) {
		@array[$j] = "$date,Receiver IP,$row,,,";
		#print "@array[$j]\n";
		$ip = $row;
		$j++;
	}
	elsif ($k == 2 && $row =~ /\d{4}-\d{2}-\d{2}/) {
		@array[$j] = "$date,Receiver Date,$ip,,,";
		#print "@array[$j]\n";
		$j++;
	}
	elsif ($k == 3 && $row =~ /\d{1,2}.\d.\d/) {
		@array[$j] = "$date,Receiver Buildstamp,$ip,$row,,";
		#print "@array[$j]\n";
		$j++;
	}
	elsif ($k == 4 && $row =~ /u0|p\d/) {
      if ($row =~ /ok/i) {
			$row =~ s/\W+/ /g;
			@array[$j] = "$date,Receiver Raid,$ip,$row,OK,";
		}
		elsif ($row =~ /fail/i) {
			@array[$j] = "$date,Receiver Raid,$ip,$row,Fail,";
		}
		#print "@array[$j]\n";
      $j++;
   }
#Testing the megaraid output
	elsif ($k == 4 && $row =~ /:\s/) {
		if ($row =~ /Enclosure Device ID/) {
			$enclosure = $row;
			$enclosure =~ m/:\s(\d{1,3})/;
			$enclosure = $1;
			#print "$enclosure\n";
		}
		elsif ($row =~ /Device Id:/) {
			$device = $row;
			$device =~ m/:\s(\d{1,2})/;
			$device = $1;
			#print "$device\n";
		}
		elsif ($row =~ /Firmware\sstate/) {
			$status = $row;
			$status =~ m/:\s(.*)/;
			$status = $1;
			$status =~ s/,/ /;
			#print "$status\n";
			if ($status =~ /Spun Up/) {
		      @array[$j] = "$date,Receiver Raid,$ip,[$enclosure:$device]$status,OK,";
			}
			else {
				@array[$j] = "$date,Receiver Raid,$ip,[$enclosure:$device]$status,Bad,";
			}
   	   #print "@array[$j]\n";
      	$j++;

		}
		
#End testing megaraid output
	}
   elsif ($k == 5 && $row =~ /dev/) {
		$row =~ s/\s+/ /g;
		my $pctuse = $row;
		#print "$row\n";
		if ($pctuse =~ m/(\b\d\d?\d?)\W\s\//) {
			$pctuse = $1;
			#print "$pctuse\n";
		}
		if ($pctuse <= 30) {
			@array[$j] = "$date,Receiver Disk,$ip,$row,good,";
		}
		elsif ($pctuse > 30 && $pctuse < 80) {
			@array[$j] = "$date,Receiver Disk,$ip,$row,average,";
		}
		elsif ($pctuse > 80) {
			@array[$j] = "$date,Receiver Disk,$ip,$row,high,";
		}
		#print "@array[$j]\n";
      $j++;
   }
   elsif ($k == 6 && $row =~ /\d/) {
		if ($row >= 70) {
			@array[$j] = "$date,Receiver CPU,$ip,The average CPU utilization is $row,high,";
		}
		elsif ($row < 70) {
			@array[$j] = "$date,Receiver CPU,$ip,The average CPU utilization is $row,OK,";
		}
      #print "@array[$j]\n";
      $j++;
   }
   elsif ($k == 7 && $row =~ /\d/) {

		if ($row >= 70) {
         @array[$j] = "$date,Receiver Disk,$ip,The average disk utilization is $row,high,";
      }
      elsif ($row < 70) {
         @array[$j] = "$date,Receiver Disk,$ip,The average disk utilization is $row,OK,";
      }
      #print "@array[$j]\n";
      $j++;
   }
   elsif ($k == 8 && $row =~ /-->\s\d{1,5},/) {
		$row =~ s/[^,]*,//;
		#print "@array[$j]\n";

      $dsdate = $row;
      $dsdate =~ m/([^,]*),\s(.*)/;
      $dsdate = $1;
      $msg = $2;
		$msg =~ s/,/ /g;
		$dsdate =~ s/\s//;
		#print"$dsdate\n$msg\n";
      @array[$j] = "$date,Receiver Red Flag,$ip,$dsdate $msg,,";
		$j++;
   }
$i++;
}
close ($fh);
system('touch /tmp/device_health');
my $filename = '/tmp/device_health';
open (my $fh, '>', $filename);
my $length = scalar @array;
my $h = 0;
while ($h < $length) {
	print $fh "@array[$h]\n";
	$h++;
}
close ($fh);
system ('rm /tmp/healthoutput.txt');
