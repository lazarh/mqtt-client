import time, board, busio
from adafruit_htu21d import HTU21D

# read sensor data
i2c = busio.I2C(board.SCL, board.SDA)
sensor = HTU21D(i2c)

def readTemp():
	return str(round(sensor.temperature, 2))

def readHumid():
	return str(round(sensor.relative_humidity, 2))

