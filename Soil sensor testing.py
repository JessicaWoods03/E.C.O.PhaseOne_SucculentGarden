#This is the tutorial testing for the soil sensor
#Just wired all my sensors and tested them individually
#Tomorrow I wire them all on the same board if I can and run it on a cron command
# to start dumping data into a database with SQLite-
#I will have photos posted on how I wired each sensor up to the bread board
import time

from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus =busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)

while True:

    #read moisture level through capacitive touch pad
    
    touch = ss.moisture_read()

    #read temperature from  the temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + " moisture: " + str(touch))
    time.sleep(1)
