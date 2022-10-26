# Phillip Misterman
# AERE 462
# DTO Code 

# TODO Implement control binds and set associated gpio pin outputs to control thrust and pulses / Investagate Pygame package as a replacement for pynput

from pynput.keyboard import Key, Listener

def show(key):

    try:
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:

        # When delete key is pressed terminate the control system connection

        if key == Key.delete:      
            return False


    print('\nYou Entered {0}'.format(key))
    print(key)

    

# Collect all inputs until termination
with Listener(on_press = show) as listener:
	listener.join()
