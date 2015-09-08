import bge
import GameLogic

calibrationParameter1 = 24
calibrationParameter2 = 2.40

try:
    serialPort = GameLogic.serialPort
    scene = bge.logic.getCurrentScene()

    letter1 = serialPort.read()
    letter2 = serialPort.read()
    letter3 = serialPort.read()
    letter4 = serialPort.read()
    letter5 = serialPort.read()
    letter6 = serialPort.read()

    intLetter1 = int(letter1)
    intLetter2 = int(letter3)
    intLetter3 = int(letter4)
    position = intLetter1 + 0.1 * intLetter2 + 0.01 * intLetter3
    
    calibratedPostion = (calibrationParameter1 * 
                        (position - calibrationParameter2))
                        
    if calibratedPostion <= -7:
        calibratedPostion = -7
    
 
except:   
    
    calibratedPostion = 0
    
scene.objects["ArmatureBody"].localPosition = [0, 0, calibratedPostion]    