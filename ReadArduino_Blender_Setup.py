import bge
import serial
import GameLogic

serialPort = serial.Serial('/dev/cu.usbmodem1411', 9600)

GameLogic.serialPort = serialPort