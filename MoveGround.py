import bge

own = bge.logic.getCurrentController().owner

moveLimit = -163
groundLength = 248

own.localPosition.x -= 0.01

if own.localPosition.x <= moveLimit:
    own.localPosition.x += 2*groundLength
