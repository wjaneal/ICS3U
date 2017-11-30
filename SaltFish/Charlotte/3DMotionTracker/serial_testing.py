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
while count < 14:
    try:
        ser.write(str(count))      # write a string
        s = ser.read(15)        # read up to ten bytes (timeout)
        
    except:
        print "Died on read"
    #line = ser.readline()   # read a '\n' terminated line
    print s, " current data"
    count += 1
ser.close()             # close port

