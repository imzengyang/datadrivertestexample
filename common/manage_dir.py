
import time
import os

def getScreenShotDir():

    return './screenshots'

def getPngfileName():
    screenshotsDir = getScreenShotDir()
    current_time = time.time()
    return screenshotsDir + str(current_time) + '.png'
    

