#import serial
import time
import requests
import json
firebase_url = 'YOUR_FIREBASE_DB_URL'
#Connect to Serial Port for communication
#ser = serial.Serial('COM15', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
fixed_interval = 10
while 1:
  try:
    #temperature value obtained from Arduino + LM35 Temp Sensor          
    temperature_c = ser.readline()
    
    #current time and date
    time_hhmmss = time.strftime('%H:%M:%S')
    date_mmddyyyy = time.strftime('%d/%m/%Y')
    
    #current location name
    temperature_location = 'Mumbai-Kandivali';
    print temperature_c + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' + temperature_location
    
    #insert record
    data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':temperature_c}
    result = requests.post(firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))
    
    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
  time.sleep(fixed_interval)
