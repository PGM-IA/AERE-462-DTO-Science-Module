from gpiozero import DigitalOutputDevice
from time import sleep

# Blue cluster

S4 = DigitalOutputDevice(25) # Thruster #4
S4.on()
sleep(0.5)
S4.off()

S3 = DigitalOutputDevice(24) # Thruster #3
S3.on()
sleep(0.5)
S3.off()

S2 = DigitalOutputDevice(18) # Thruster #2
S2.on()
sleep(0.5)
S2.off()

S1 = DigitalOutputDevice(17) # Thruster #1
S1.on()
sleep(0.5)
S1.off()

# Grey cluster Thrusters 5-8 verified and labeled

S8 = DigitalOutputDevice(22) # Thruster #8
S8.on()
sleep(0.5)
S8.off()

S7 = DigitalOutputDevice(23) # Thruster #7
S7.on()
sleep(0.5)
S7.off()

S6 = DigitalOutputDevice(16) # Thruster #6
S6.on()
sleep(0.5)
S6.off()

S5 = DigitalOutputDevice(5) # Thruster #5
S5.on()
sleep(0.5)
S5.off()

# Yellow cluster

S12 = DigitalOutputDevice(4) # Thruster #12
S12.on()
sleep(0.5)
S12.off()

S11 = DigitalOutputDevice(19) # Thruster #11
S11.on()
sleep(0.5)
S11.off()

S10 = DigitalOutputDevice(20) # Thruster #10
S10.on()
sleep(0.5)
S10.off()

S9 = DigitalOutputDevice(12) # Thruster #9
S9.on()
sleep(0.5)
S9.off()

# Red cluster

S16 = DigitalOutputDevice(26) # Thruster #16
S16.on()
sleep(0.5)
S16.off()

S15 = DigitalOutputDevice(13) # Thruster #15
S15.on()
sleep(0.5)
S15.off()

S14 = DigitalOutputDevice(21) # Thruster #14
S14.on()
sleep(0.5)
S14.off()

S13 = DigitalOutputDevice(27) # Thruster #13
S13.on()
sleep(0.5)
S13.off()