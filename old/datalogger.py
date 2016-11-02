## import the serial library
import serial

## Boolean variable that will represent 
## whether or not the arduino is connected
connected = False

## establish connection to the serial port that your arduino 
## is connected to.

locations=['/dev/ttyACM0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3']

for device in locations:
    try:
<<<<<<< HEAD
        print "Trying...",device
        ser = serial.Serial(device, 9600)
        break
    except:
        print "Failed to connect on",device
=======
        print ("Trying...",device)
        ser = serial.Serial(device, 9600)
        break
    except:
        print ("Failed to connect on",device)
>>>>>>> 3f64185684b124bfef7f4448f1e65d6806020986

## loop until the arduino tells us it is ready
while not connected:
    serin = ser.read()
    connected = True

## open text file to store the current 
##gps co-ordinates received from the rover    
text_file = open("samples2.csv", 'w')
## read serial data from arduino and 
## write it to the text file 'position.txt'
while 1:
    if ser.inWaiting():
        x=ser.read()
        print(x) 
        text_file.write(x)
        if x=="\b":
             text_file.seek(0)
             text_file.truncate()
        text_file.flush()

## close the serial connection and text file
text_file.close()
ser.close()