#ADBeta 
#26 Aug 2022
#Version 0.9

import midi
import sound
import time

# Init #########################################################################
#Open the midi device with the selected port
midi.open(1);

# Main program loop ############################################################
print("Polling the MIDI Device. Press Control-C to exit.")
try:
	timer = time.time()
	while True:
		midi.poll();
			
		time.sleep(0.0005)
except KeyboardInterrupt:
	print('')

# Cleanup ######################################################################	
finally:
	midi.close()



