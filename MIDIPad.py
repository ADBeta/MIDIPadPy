#ADBeta 
#26 Aug 2022
#Version 0.93

import midi
import sound
import lighting

import time

#TODO Controller config, define "stop all", "shift" etc, and control sliders etc
#TODO Load config. Probably a rev 2 upgrade

# Hard define soundboard #######################################################
sound.loadWave(1, "./kick.wav")
sound.loadWave(2, "./snare.wav")
sound.loadWave(3, "./cowbell.wav")

# Init #########################################################################
#Open the midi device with the selected port
midi.open(1);

#Refresh the lighting on the MIDI device
lighting.refresh()

# Main program loop ############################################################
print("Polling the MIDI Device. Press Control-C to exit.")
try:
	timer = time.time()
	while True:
		#Poll the MIDI device for an event message, returns mesage type
		eventType = midi.poll()

		#Key event
		if eventType == 1:			
			#Do key light event - If output is enabled
			lighting.set(midi.EventKeyIn.s, midi.EventKeyIn.p)
			
			#Create sound, takes current sound mode into account
			sound.playFromKey(midi.EventKeyIn.s, midi.EventKeyIn.p)
			
			
		#TODO Control event
			
		time.sleep(0.0005)
except KeyboardInterrupt:
	print('')

# Cleanup ######################################################################	
finally:
	#Clear the lights on the MIDI Device
	lighting.clear()
	#Close the MIDI tunnel neatly	
	midi.close()


