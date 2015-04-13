import bge
import random

scene = bge.logic.getCurrentScene()
own = bge.logic.getCurrentController().owner

r = random.random()

if r<=0.1:
    scene.addObject("Icosphere1", own)
elif (r>0.1 and r<=0.2):
    scene.addObject("Icosphere2", own)
elif (r<0.2 and r<=0.3):
    scene.addObject("Icosphere3", own)
elif (r<0.3 and r<=0.4):
    scene.addObject("Icosphere4", own)
elif (r<0.4 and r<=0.5):
    scene.addObject("Icosphere5", own)
else:
    scene.addObject("Icosphere6", own)