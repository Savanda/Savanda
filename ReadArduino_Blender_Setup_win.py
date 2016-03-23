import bge
import serial
import GameLogic

serialPort = serial.Serial('COM4', 9600)

GameLogic.serialPort = serialPort