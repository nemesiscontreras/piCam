#picamera picture capture vamped

#import all the modules needed

from picamera import PiCamera
import time
from time import sleep
from time import  strftime

camera()=PiCamera()

#time variables

camera.start_preview()

for i in range(5):
    sleep(3)
    time=strftime("_%d_%b_%H:%M:%S")
    camera.capture('/home/pi/Desktop/image%s.jpg' %time)
    
camera.stop_preview()
