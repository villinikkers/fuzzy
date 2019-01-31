import serial
import time
from sys import argv

testName = argv[1]

logfile = 'Logs\\' + testName + '.txt'


print(f"""Starting temperature logging.
Logfile will be saved in {logfile}.
To stop the temperature logging press Ctrl+c.\n""")
with serial.Serial('COM7', 9600, timeout = 1) as ser:
    with open(logfile, 'w') as log:
        while 1:
            tempTime = time.localtime()
            temp = ser.readline()
            temp = temp.decode('utf-8')
            timestamp = f"{tempTime[3]}:{tempTime[4]} - {temp}"
            print(timestamp)
            log.write(timestamp)
            time.sleep(0.5)
