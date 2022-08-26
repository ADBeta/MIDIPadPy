#Import function to send MIDI data to the MIDI Device
from midi import send

import time

# Lighting Variables ###########################################################
#Background 'default' colour of each button
idleKeyColour = [0] * 127

#'pressed' colour of each button
pressedKeyColour = [5] * 127

#Refresh all the lighting on the MIDI device. uses idleKey and pressedKey
def refresh():
	for x in range(0, 127):
		send(144, x, idleKeyColour[x])
		#Small delay
		time.sleep(0.0001)

def clear():
	for x in range(0, 127):
		send(144, x, 0)
		#Small delay
		time.sleep(0.0001)

#Set specific key colour
def set(status: int, key: int):
	if status == 144: #Pressed
		send(144, key, pressedKeyColour[key])
	
	if status == 128: #Released
		send(144, key, idleKeyColour[key])
	
