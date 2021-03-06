# AlarmLogsCleaner
### _Reading alarm logs just became easier !!!_

AlarmLogsCleaner is a python-based tool that scans each line of the alarm log file, extracts only the critical pieces of information and dumps them into a new file

To illustrate with an example, below are a few lines from the original alarm log file taken from a lab router

```sh
<s neid="3912" key="//object=slot//slot=ts5" cause="Equipment-Detected" addtionalinfo="null" severity="warning" category="eqpt" gentime="2020-02-05,08:38:04"></s>
<s neid="3912" key="//object=slot//slot=ts4" cause="Equipment-Detected" addtionalinfo="null" severity="warning" category="eqpt" gentime="2020-02-05,08:38:04"></s>
<s neid="3912" key="//object=slot//slot=ts3" cause="Equipment-Detected" addtionalinfo="null" severity="warning" category="eqpt" gentime="2020-02-05,08:38:04"></s>
<s neid="3912" key="//object=slot//slot=ts1" cause="Equipment-Detected" addtionalinfo="null" severity="warning" category="eqpt" gentime="2020-02-05,08:38:04"></s>
<s neid="3912" key="//object=card//slot=xsb" cause="Card-Ctrl-Fail" addtionalinfo="null" severity="critical" category="eqpt" gentime="2020-02-05,08:52:00"></s>
```

After running this file through this tool, the lines will be as below

```sh
object=slot//slot=ts5 || Equipment-Detected || gentime= 2020-02-05,08:38:04
object=slot//slot=ts4 || Equipment-Detected || gentime= 2020-02-05,08:38:04
object=slot//slot=ts3 || Equipment-Detected || gentime= 2020-02-05,08:38:04
object=slot//slot=ts1 || Equipment-Detected || gentime= 2020-02-05,08:38:04
object=card//slot=xsb || Card-Ctrl-Fail || gentime= 2020-02-05,08:52:00
```

## Requirements
Linux machine with python 2.7 installed

## How to use
Clone this file from the repo, give it executable permissions and run it without any arguments

#### Note: 
The original alarm logs folder must be in the same directory where the script is present

```sh
[user@localhost]# ./alarm_logs_cleaner.py 

Enter alarm logs folder name: router1_alarm_logs


Cleaning file router1_alarm_logs/alm_log2.xml...
Done


Cleaning file router1_alarm_logs/alm_log4.xml...
Done


Cleaning file router1_alarm_logs/alm_log3.xml...
Done


Cleaning file router1_alarm_logs/alm_log0.xml...
Done


Cleaning file router1_alarm_logs/alm_log1.xml...
Done


Logs saved to /tmp/router1_alarm_logs/

[user@localhost]#
```
