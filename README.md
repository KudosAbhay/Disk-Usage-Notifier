# ifttt-webhook-Disk-Usage-Analyzer

An IFTTT-Webhook for receiving emails automatically if your Disk Usage exceeds 90% in Ubuntu

<br>
**Basic Dependencies**:
* You must be using Ubuntu or any OS version which is based on Ubuntu v14.04 or above
* You must have installed python3 or above versions
* You must have one working email account

<br>
**To make this work, follow these steps**
1.  Download the repo using ```git clone https://github.com/KudosAbhay/ifttt-webhook-Disk-Usage-Analyzer.git```
2.  Create an account on [IFTTT](https://ifttt.com/)
3.  Create an IFTTT Webhook
  * Go to My Applets
  * Click on Create New Applet
  * Click on the <b>“+”</b> sign in the statement <i>“If <b>+ this </b> then <b>that</b></i>”
  * Type <b>‘webhook’</b> and select <b>Webhooks</b>
  * Click on ‘<b>Receive a Web Request</b>‘ option
  * Enter Event Name
  * Hit ‘<b>Create Trigger</b>’
  * Now click on <b>“+”</b> sign in the statement <i>“If <b>this</b> then <b>+ that </b>”</i>
  * Type <b>‘Gmail‘</b> and select it
  * Click on <b>‘Send an Email’</b>
  * Type your email ID. Type ``` {{Value1}} ``` in <b>To address</b>, ``` {{Value2}} ``` in <b>CC address</b>, write any subject you want and in the Body Section type ``` {{Value3}} ```.
  * Note Down the IFTTT Trigger Name (i.e Event Name which you have used for this Applet)
  * Select <b>Finish</b>. Your ifttt-webhook is ready to be fired!
4.  Note Down the IFTTT Key which you get [visit here](https://ifttt.com/maker_webhooks) and Click on Documentation Button
5.  Insert Trigger Name, IFTTT Key, Your Email ID, Other Email ID to which CC shall be mailed in the Python Code
6.  Now run the code and see the output. If your Disk Usage has exceeded 90% in any of the disks, then you will receive an email.



# To keep this running automatically in background on Ubuntu:
1.  Type ``` chmod a+x Disk-Usage-Analyzer.py``` by going to the repo folder. This will make it executable.
2.  Type ``` crontab -e ``` to open crontab editor.
3.  To Run this program every minute use ``` */1 * * * * /usr/bin/python3 /folder/location/Disk-Usage-Analyzer.py ``` in crontab
4.  Done! Disk-Usage-Analyzer.py can now send an email automatically at that specified time which you have mentioned in crontab if your Disk Usage exceeds more than 90%.



