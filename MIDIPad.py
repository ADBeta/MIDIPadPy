#ADBeta 
#25 Aug 2022
#Version 0.9

import midi
import time

# Init #########################################################################
#Open the midi device with the selected port
midi.open(1);

print("Polling the MIDI Device. Press Control-C to exit.")

# Main program loop ############################################################
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



