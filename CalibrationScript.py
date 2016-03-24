import serial

serialPort = serial.Serial('/dev/cu.usbmodem1411', 9600)

ii = 0
positionAccumulation = 0

for i in range(0,9):
    ii += 1
    try:
        letter1 = serialPort.read()
        letter2 = serialPort.read()
        letter3 = serialPort.read()
        letter4 = serialPort.read()
        letter5 = serialPort.read()
        letter6 = serialPort.read()
        intLetter1 = int(letter1)
        intLetter2 = int(letter3)
        intLetter3 = int(letter4)
        positionAccumulation += intLetter1 + 0.1 * intLetter2 + 0.01 * intLetter3
    except:
        ii -= 1   

position = positionAccumulation/ii   
                        
print("Signal from Arduino", position)