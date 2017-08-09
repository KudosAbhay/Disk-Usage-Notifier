# ifttt-webhook-Disk-Usage-Analyzer
An IFTTT-Webhook for receiving email automatically if your Disk Usage exceeds 90% in Ubuntu

# Steps to create and use this python code:
1.  Download the repo using ```git clone https://github.com/KudosAbhay/ifttt-webhook-Disk-Usage-Analyzer.git```
2.  Create an account on [IFTTT](https://ifttt.com/)
3.  Read the [Documentation file](https://github.com/KudosAbhay/ifttt-webhook-Disk-Usage-Analyzer/blob/master/Steps%20to%20make%20an%20ifttt-webhook%20to%20send%20email.txt) provided and create an IFTTT-Webhook 
4.  Note Down the IFTTT Trigger Name (Event Name)
5.  Note Down the IFTTT Key which you get [visit here](https://ifttt.com/maker_webhooks) and Click on Documentation Button
6.  Insert Trigger Name, IFTTT Key, Your Email ID, Other Email ID to which CC shall be mailed in the Python Code
7.  Now run the code and see the output. If your Disk Usage has exceeded 90% in any of the disks, then you will receive an email.



# To keep this running automatically in background on Ubuntu:
1.  Type ``` crontab -e ``` in console.
2.  Provide the timing, location of python installed in your Ubuntu and location of this downloaded repo in crontab. Save it.
3.  Type ``` chmod a+x Disk-Usage-Analyzer.py``` by going to the repo folder. This will make it executable.
4.  ```Disk-Usage-Analyzer.py``` now send an email automatically at that specified time which you mentioned in crontab if your Disk Usage exceeds more than 90%.



