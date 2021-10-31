#!/usr/bin/env python

################################################################
#							       #
#   Name:    alarm_logs_cleaner.py			       #
#							       #
#   Purpose: This script will remove unnecessary information   #
#            from the alarm log files making the files         #
#	     more readable for the user                        #
#							       #
#   Usage:   ./alarm_logs_cleaner.py                           #
#							       #	       
#	     The original alarm logs folder must be in the     # 
#	     same directory where the script is present        #
#                                                              #
################################################################

import sys, os, re
from os.path import join

def cleanline(line):

	if 'severity="cleared"' not in line:

		a = line.split()[2].replace('key=','').replace('"','').replace('//','',1)
		b = line.split()[3].replace('cause=','').replace('"','')
		c = line.split()[7].split('>')[0].replace('"','').replace('gentime=','gentime= ')

		return a + ' || ' + b + ' || ' + c

	else:

		a = line.split()[2].replace('key=','').replace('"','').replace('//','',1)
		b = line.split()[3].replace('cause=','').replace('"','')
		c = line.split()[7].split('>')[0].replace('"','').replace('gentime=','cleartime= ')

		return a + ' || ' + b + ' || ' + c


####### MAIN PROGRAM STARTS HERE #######

print ""

folder = raw_input("Enter alarm logs folder name: ")

print ""

new_folder_name = '/tmp/' + folder + '/'

os.mkdir(new_folder_name)

filelist = []


for x,y,z in os.walk(folder):

	for file in z:

		if re.search(r"^alm_log(\d+)\.xml", file):

			filelist.append(join(x,file))


for file in filelist:

	print "\nCleaning file {}...".format(file)
 
	fd = open('/tmp/' + file,'w')

	for line in open(file,'r'):

		#print 'original' + line

		fd.write(cleanline(line) + "\n")

	fd.close()

	print "Done\n"

print "\nLogs saved to {}\n".format(new_folder_name)
