from picamera import PiCamera
from time import sleep
from datetime import datetime

#This is the time stamp for the file name %m = month, %d = day, %H =hour, %M = min
name = datetime.now().strftime("%m-%d_%H:%M")

camera = PiCamera()

camera.start_preview()
sleep(5)
#This is the path name to the file you want to save images to, with the time stamp called "name"
#With the type of file .jpg
#This is ran every hour through the cron command
#This path runs to the SSD drive to save space on my pi
camera.capture('/media/pi/a64c97e2-ea3f-4ce2-a1e5-c70ab45f51c1/Infrared_images/' + name + '.jpg')
camera.stop_preview()
