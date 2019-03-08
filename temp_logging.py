#This works on Rasperry pi running python3.5
import serial
import time
from sys import argv


testName = input('Name the log file:\n>')

logfile = "Logs/" + testName + ".csv"


print("Starting temperature logging.\nLogfile will be saved in {}.\
To stop the temperature logging press Ctrl+c.\n".format(logfile))

# linux: change COM7 with: '/dev/ttyUSB0'
with serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) as ser:
    with open(logfile, 'w') as log:
        header = "Time;Temp 1; Temp 2\n"
        log.write(header)
        while 1:
            tempTime = time.localtime()
            #h = str(tempTime[3]).zfill(2)
            #m = str(tempTime[4]).zfill(2)
            timestamp = time.strftime('%d-%m-%y %H:%m', tempTime)
            temp = ser.readline()
            temp = temp.decode('utf-8')
            logline = "{};{}\n".format(timestamp,temp)
            print("{} - {}".format(timestamp, temp))
            log.write(logline)
            time.sleep(600)
