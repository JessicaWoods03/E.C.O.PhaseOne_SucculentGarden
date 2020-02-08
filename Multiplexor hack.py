#mulitplexor hack for sensors in python, have to adjust my database for error.
#will change print statements to save it to the database. This lets me know
#that its working

import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

#these are magic global variables that are used, my PORT_SOIL_SENSOR_1 is in
# SC5, SD5 = port 5 on the multiplexor, PORT_SOIL_SENSOR_2 is in SC2, SD2 =port2
#on the multplexor,  made the i2c_bus global as well.
PORT_SOIL_SENSOR_1 = 5
PORT_SOIL_SENSOR_2 = 2
i2c_bus =busio.I2C(SCL, SDA)


def soil_reading():
    #read moisture level through capacitive touch pad
    ss = Seesaw(i2c_bus, addr=0x36)
    touch = ss.moisture_read()
    time.sleep(1)
    touch2 = ss.moisture_read()
    difference = touch - touch2

    #check sensor for daily errors
    if (difference > 3 or difference < -3):
        print("moisture warning", difference)

    

    #read temperature from  the temperature from the temperature sensor
    temp = ss.get_temp()
    time.sleep(1)
    temp2 = ss.get_temp()
    temp_difference = temp - temp2

    #check sensor for daily errors
    if (temp_difference > 3 or temp_difference < -3):
        print("tempurature warning", temp_difference)
    
    print("temp: ",temp, " moisture: ",touch)
    time.sleep(1)


def soil_sensor(port):
    
    #commands for soil sensor 1
    buffer = bytearray(1)
    buffer[0] = 1 << port
    i2c_bus.writeto(0x70,buffer,start=0,end=len(buffer),stop=True)
    soil_reading()
    

def main():
    
    #With the aid of this website:https://circuitpython
    #.readthedocs.io/en/2.x/shared-bindings/busio/I2C.html
    #I brainstormed with a friend to understand the concept behind the code
    soil_sensor(PORT_SOIL_SENSOR_1)
    soil_sensor(PORT_SOIL_SENSOR_2)

main()




