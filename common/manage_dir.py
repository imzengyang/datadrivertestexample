
import time
import os

# 可以进一步进行优化操作
def getScreenShotDir():
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    rootdir = os.path.split(current_file_dir)[0]
    newdir= os.path.join(rootdir,"screenshots")
    if os.path.exists(newdir):
        print('ok')
    else:
        os.mkdir(newdir)
    return newdir

def getPngfileName():
    screenshotsDir = getScreenShotDir()
    current_time = time.time()

    # TODO filename 2018_05_27_15_48_30.png
    # http://www.runoob.com/python/python-date-time.html
    filename = os.path.join(screenshotsDir,str(current_time)+'.png')
    return filename


    