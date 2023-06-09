import time
import board
import busio
import sys 
import adafruit_ads1x15.ads1115 as ADS 
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)

# Create differential input between channel 0 and 1
chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("1: {:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
    print("2: {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
    time.sleep(0.5)