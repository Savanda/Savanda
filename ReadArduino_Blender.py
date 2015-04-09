import serial
import time
import signal
import sys
import bpy

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
#try:
i = 0
while i<20:
    i += 1
    p1 = ser.read()
    p2 = ser.read()
    p3 = ser.read()
    p4 = ser.read()
    p5 = ser.read()
    p6 = ser.read()
    print(p1,p2,p3,p4,p5,p6)
    ip1 = int(p1)
    ip2 = int(p3)
    ip3 = int(p4)
    t = ip1 + 0.1*ip2 + 0.01*ip3
    print(t)
    
    tt = 14*(t - 2.55)
    print(tt)
    
    #bpy.data.objects["Cube"].location = (0,0,tt)

    
#except (KeyboardInterrupt, SystemExit):
#    raise
