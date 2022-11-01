# Phillip Misterman
# AERE 462
# DTO Control Code

# Import required modules
from gpiozero import DigitalOutputDevice
from time import sleep
import pygame
import sys

# initialising pygame
pygame.init()

# Define Global Variables

# Default Pulse Duration
pulse_dir = 0.400

#   Define Keybinds:
#       Motion Controls
translational = [pygame.K_h, pygame.K_n, pygame.K_l, pygame.K_j, pygame.K_i, pygame.K_k]
rotational = [pygame.K_e, pygame.K_q, pygame.K_s, pygame.K_w, pygame.K_a, pygame.K_d]

#       Thrust Modulation
pulse_modulate = [pygame.K_PLUS, pygame.K_MINUS, pygame.K_x]

#       Termination of mission
abort_mission = pygame.K_DELETE
mission_end = False

#   Define Pin and Thruster Numbers(S# = thruster number)

#       Blue Cluster
S1  = DigitalOutputDevice(17)
S2  = DigitalOutputDevice(18)
S3  = DigitalOutputDevice(24)
S4  = DigitalOutputDevice(25)

#       Grey Cluster
S5  = DigitalOutputDevice(5)
S6  = DigitalOutputDevice(16)
S7  = DigitalOutputDevice(23)
S8  = DigitalOutputDevice(22)

#       Yellow Cluster
S9  = DigitalOutputDevice(12)
S10 = DigitalOutputDevice(20)
S11 = DigitalOutputDevice(19)
S12 = DigitalOutputDevice(4)

#       Red Cluster
S13 = DigitalOutputDevice(27)
S14 = DigitalOutputDevice(21)
S15 = DigitalOutputDevice(13)
S16 = DigitalOutputDevice(26)

# Create Functions for 6 DoF, propulsion control and system start up.

#   Closes all valves/sets all pin to low
def close_all_valves():

    S1.off()
    S2.off()
    S3.off()
    S4.off()

    S5.off()
    S6.off()
    S7.off()
    S8.off()

    S9.off()
    S10.off()
    S11.off()
    S12.off()

    S13.off()
    S14.off()
    S15.off()
    S16.off()

#   Translational motion functions

def translation(pulse_dir,key): # Movement in the x+ direction with a pulse of pulse_dir

    # X direction

    if(key == pygame.K_h): # X+

        S3.on()
        S7.on()
        S12.on()
        S15.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_n): # X-

        S1.on()
        S5.on()
        S9.on()
        S13.on()
        sleep(pulse_dir)
        close_all_valves()

    # Y direction

    elif(key == pygame.K_l): # Y+

        S6.on()
        S16.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_j): # Y-

        S8.on()
        S14.on()
        sleep(pulse_dir)
        close_all_valves()

    # Z direction

    elif(key == pygame.K_i): # Z+

        S4.on()
        S10.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_k): # Z-

        S2.on()
        S12.on()
        sleep(pulse_dir)
        close_all_valves()
    
#   Rotational motion functions

def Rotation(pulse_dir,key): # Movement in the x+ direction with a pulse of pulse_dir

    # X direction

    if(key == pygame.K_e): # X+ (CW)

        S4.on()
        S8.on()
        S12.on()
        S16.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_q): # X- (CCW)

        S2.on()
        S6.on()
        S10.on()
        S14.on()
        sleep(pulse_dir)
        close_all_valves()

    # Y direction

    elif(key == pygame.K_s): # Y+

        S7.on()
        S13.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_w): # Y-

        S5.on()
        S15.on()
        sleep(pulse_dir)
        close_all_valves()

    # Z direction

    elif(key == pygame.K_a): # Z+

        S1.on()
        S11.on()
        sleep(pulse_dir)
        close_all_valves()

    elif(key == pygame.K_d): # Z-

        S3.on()
        S9.on()
        sleep(pulse_dir)
        close_all_valves()

# End defs and begin main body

# Set all pins to low
close_all_valves()

# Create "HUD"
display = pygame.display.set_mode((300, 300))

while  not mission_end:
    
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key in translational:
                translation(pulse_dir,event.key)
            
            if event.key == pygame.K_DELETE:
                pygame.quit()
                sys.exit()  
			
			