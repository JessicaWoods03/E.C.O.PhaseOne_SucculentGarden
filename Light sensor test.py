import time
import busio
import board
import adafruit_veml6070 

with busio.I2C(board.SCL, board.SDA) as i2c:
    uv = adafruit_veml6070.VEML6070(i2c)
    print(dir(uv))
    uv_raw = uv.uv_raw
    risk_level = uv.get_index(uv_raw)

print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))
