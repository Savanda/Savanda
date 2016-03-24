import bge
import GameLogic

signalExhale = 1.54
signalInhale = 2.24

positionBirdTop = 4
positionBirdBottom = -7

calibrationParameter1 = (positionBirdTop - positionBirdBottom)/(signalInhale - signalExhale)
calibrationParameter2 = (signalInhale * positionBirdBottom - signalExhale * positionBirdTop)/(signalInhale - signalExhale)

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
    
    calibratedPostion = calibrationParameter2 + calibrationParameter1 * position
                        
    if calibratedPostion <= positionBirdBottom:
        calibratedPostion = positionBirdBottom

    if calibratedPostion > positionBirdTop:
        calibratedPostion = positionBirdTop
    
 
except:   
    
    calibratedPostion = 0
    
scene.objects["ArmatureBody"].localPosition = [0, 0, calibratedPostion]    