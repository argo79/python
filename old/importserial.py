import serial, os, time

ser = serial.Serial('/dev/ttyACM0',9600)
<<<<<<< HEAD
os.getcwd()

for line in open('/home/argo2/samples.csv'):
   ser.read(line)
   time.sleep(3)
=======
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
>>>>>>> 3f64185684b124bfef7f4448f1e65d6806020986
