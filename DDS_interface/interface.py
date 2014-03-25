import serial
# import sysconfig


ddsSerial = serial.Serial
# ddsSerial.port
ddsSerial.baudrate=115200

try:
    ddsSerial.open()
    except SerialException
        print 'unable to open serial port', ddsSerial.port
        exit
    
    
