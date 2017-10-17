import os
import http.client

email = "your-email@gmail.com"
cc_email = "cc@gmail.com"
threshold_value = "90"
message_to_post = "Your Disk Usage has Exceeded 90%"




#Checking Disk Usage
df_output_lines = [s.split() for s in os.popen("df -Ph").read().splitlines()]
#Setting Threshold Value
threshold = float(threshold_value)/100;
#Measure the Length of Output obtained from checking Disk-Usage
array_length = len(df_output_lines)

for i in range(array_length):
    print("{}, {}, {}".format(df_output_lines[i][0] , df_output_lines[i][1]  , df_output_lines[i][4] ))
    count = df_output_lines[i][4].find('%')
    if(count < 3):
        variable = df_output_lines[i][4]
        #Trim the Value string and get the Substring till '%' sign
        variable = variable[0:count]
        #Convert the Substring value to float and then calculate it's percentage
        temp = float(variable)/100
        #Check if this value is > Threshold Value
        if(temp > threshold):
            conn = http.client.HTTPSConnection("maker.ifttt.com")
            payload = "{\n\t\"value1\" : \""+email+"\",\n\t\"value2\" : \""+cc_email+"\",\n\t\"value3\" : \""+message_to_post+"\"\n}"
            headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
            conn.request("POST", "/trigger/Disk_Usage_Exceeded/with/key/pb6iH8iLldXveE6cp4EgA9eJhAvW6CwGzL4q77mI-iR", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
		#print("{} is PERCENTAGE".format(df_output_lines[i][4]))
    else:
        print("SKIPPING THIS VALUE")
