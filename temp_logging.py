# Developed to run on python 3.7
import serial
import time
from sys import argv

testName = input("Name the logfile:\n>")


logfile = 'Logs/' + testName + '.csv'


print(f"""Starting temperature logging.
Logfile will be saved in {logfile}.
To stop the temperature logging press Ctrl+c.\n""")
with serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) as ser:
    with open(logfile, 'w') as log:
        header = "Timestamp\tSensor 1\tSensor 2\n"
        log.write(header)
        time.sleep(0.5)
        while 1:
            time.sleep(2)
            tempTime = time.localtime()
            temp = ser.readline().decode('utf-8')
            #temp = temp.decode('utf-8')
            timestamp = f"{tempTime[3]}:{tempTime[4]}\t{temp}\t{temp}"
            print(timestamp)
            log.write(timestamp)
