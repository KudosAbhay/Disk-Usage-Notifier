# Disk-Usage-Notifier

An IFTTT-Webhook for receiving emails automatically if your Disk Usage exceeds 90% in Ubuntu v14 and above.

<br>

**Basic Dependencies**:
* You must be using Ubuntu or any OS version which is based on Ubuntu v14.04 or above
* You must have installed python3 or above versions

<br>

**To make this work, follow these steps**
1.  Download the repo using ```git clone https://github.com/KudosAbhay/Disk-Usage-Notifier.git```
5.  Insert your Email ID, Other Email ID which must receive a carbon copy of the same in the main Python Code on Line 29
6.  Now run the code and see the output. If your Disk Usage has exceeded 90% in any of the disks, then you will receive an email.



# To keep this running automatically in background on Ubuntu:
1.  Type ``` chmod a+x Disk-Usage-Notifier.py``` by going to the repo folder. This will make it executable.
2.  Type ``` crontab -e ``` to open crontab editor.
3.  To Run this program every minute use ``` */1 * * * * /usr/bin/python3 /folder/location/Disk-Usage-Notifier.py ``` in crontab
4.  Done! Your Disk-Usage-Notifier can now send an email automatically at that specified time which you have mentioned in crontab if your Disk Usage exceeds more than 90%.



