import serial, os, time

ser = serial.Serial('/dev/ttyACM0',9600)
#os.getcwd()
import time
file = open('ritardi.csv')
while 1:
	line = file.readline()
	if not line:
		  break
	ser.write(line)
	time.sleep(3)
file.close