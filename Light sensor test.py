import time
import busio
import board
import adafruit_veml6070 

# Make sure your i2c is configured on your raspberry pi for your sensor boards
# if not follow this website https://learn.adafruit.com/
# adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

with busio.I2C(board.SCL, board.SDA) as i2c:
    uv = adafruit_veml6070.VEML6070(i2c)
    
    #this tells you available commands for the sensor
    print(dir(uv))
    
    #on the pdf and tutorial uv.read is unavaible, so tried this and it works
    uv_raw = uv.uv_raw
    risk_level = uv.get_index(uv_raw)

print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))
