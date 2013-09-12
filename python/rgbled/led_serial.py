import serial

ser = serial.Serial('/dev/cu.usbserial-A8008Kkm', 9600)  # for USB on Mac OS X. Update to reflect the right serial port
                                                         # on your machine

ser.read()  # was needed in initial setup as arduino indicates that it's ready
