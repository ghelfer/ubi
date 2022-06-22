import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
 
while True:
    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    time.sleep(2)
    

 #  Define application commands and features:
def _range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
def evaluateSensorValue():
    # Test your module, then define the value range - in this case between 0 and 60000.
    sensorValue = _range(channel_0.value, 0, 60000, 0, 1023)
    sensor_value.value = sensorValue
    # Threshold
    if(sensorValue > 300):
        status_text.value = "Status: DANGER"
        status_text.text_color = "yellow"
        warn("!!!DANGER!!!", "Air Quality Deteriorating!")
    else:
        status_text.value = "Status: OK"
        status_text.text_color = "green"
 

