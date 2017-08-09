import os
import http.client

#Check Disk Usage by issuing a command 'df -h' for Ubuntu
df_output_lines = [s.split() for s in os.popen("df -Ph").read().splitlines()]
#print(df_output_lines[1:])

#Store a Threshold Value for 90% in a variable
threshold = float(90)/100;
#print(threshold)

#Measure the Length of Output obtained from the command 'df -h'
array_length = len(df_output_lines)
#print(array_length)

for i in range(array_length):
    print("{}, {}, {}".format(df_output_lines[i][0] , df_output_lines[i][1]  , df_output_lines[i][4] ))
    count = df_output_lines[i][4].find('%')
    if(count < 3):
        variable = df_output_lines[i][4]
        #Trim the Value string and get the Substring till '%' sign
        variable = variable[0:count]
        #Convert the Substring value to float and then calculate it's percentage
        temp = float(variable)/100
        #print(temp)
        #Check if this value is > 90%
        if(temp > threshold):
            conn = http.client.HTTPSConnection("maker.ifttt.com")
            payload = "{\n\t\"value1\" : \"yourEmailID@youremail.com\",\n\t\"value2\" : \"cctoSomeone@email.com\",\n\t\"value3\" : \"Usage of your Disk has exceeded more than 90% on your EC2 Instance\"\n}"
            headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            #'postman-token': "1e31a613-7d04-4b04-b663-1b38179cd3f6"
            }
            conn.request("POST", "/trigger/your_IFTTT_Trigger/with/key/your_IFTTT_Key", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
		#print("{} is PERCENTAGE".format(df_output_lines[i][4]))
    else:
        print("SKIPPING THIS VALUE")
