#Python serial (USB COM) Testing program
#May 7, 2009

import serial

ser = serial.Serial(4, baudrate=9600, timeout=4)  # open first serial port
print ser.portstr       # check whicH port was really used
try:
    print "Writing character"
    ser.write("6")      # write a string  
except:
    print "Could not connect"
count = 0
while count < 140:
    try:
        #May 8, 2009:  write a protocol for the arduino to receive a '-1'
        #and then read the next two bytes immediately
        ser.write(str(8))      # write a string
        ser.write(str(9))
        s = ser.read(15)        # read up to ten bytes (timeout)
        line = ser.readline()   # read a '\n' terminated line
    except:
        print "Died on read"
    #line = ser.readline()   # read a '\n' terminated line
    print s, " current data"
    count += 1
ser.close()             # close port

