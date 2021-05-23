
from time import *
import RPi.GPIO as GPIO
import spidev

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000

# adc
def read_spi_adc(adcChannel):
    adcValue=0
    buff = spi.xfer2([1, (8+adcChannel)<<4, 0])
    adcValue = ((buff[1]&3)<<8)+buff[2]
    return adcValue

def map(value, min_adc, max_adc, min_hum, max_hum):
    adc_range = max_adc-min_adc
    hum_range = max_hum-min_hum
    scale_factor = float(adc_range)/float(hum_range)
    return min_hum+((value-min_adc)/scale_factor)

try:
    adcChannel=0
    while True:
        adcValue = read_spi_adc(adcChannel)
        V = int(map(adcValue, 0, 1023, 0, 1000))
        print(V)
        sleep(1)
finally:
    GPIO.cleanup()
    spi.close()
