from picamera import PiCamera
from time import sleep
from datetime import datetime
name = datetime.now().strftime("%h_%d_%m")

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/' + name + '.jpg')
camera.stop_preview()
