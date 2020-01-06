import board
import busio
import adafruit_bme680
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

#Testing using the Adafruit tutorial for the BME680 board
#This board requires a 24 hours of runtime to normalize for accurate readings
#meaning if you set your cron commands to run the board on a time interval then
#it would need to do that for 24 hours before I would trust the data-

print('Temperature : {} degrees C'.format(sensor.temperature))
print('Gas: {} ohms'.format(sensor.gas))
print('Humidity: {}%'.format(sensor.humidity))
print('Pressure: {}hPa'.format(sensor.pressure))

sensor.sea_level1hPa = 1014.5

print('Altitude: {} meters'.format(sensor.altitude))
