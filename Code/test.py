from gpiozero import DigitalOutputDevice
from time import sleep

S1 = DigitalOutputDevice(13) # Thruster #15
S1.on()
sleep(30)
S1.off()