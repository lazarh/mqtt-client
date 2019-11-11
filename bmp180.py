#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library

# Create an 'object' containing the BMP180 data
sensor = BMP085.BMP085()

def readTemp():
    return str(round(sensor.read_temperature(), 2))

def readPressure():
    return int(sensor.read_pressure())

def readAltitude():
    return str(round(sensor.read_altitude(), 2))

def readSealevelPressure():
    return sensor.read_sealevel_pressure

#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature())) 
#print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())) 
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#print( 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
