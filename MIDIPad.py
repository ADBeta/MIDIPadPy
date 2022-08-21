#ADBeta 
#21 Aug 2022
#Version 0.7

import midi

#Open the midi device with the selected port
midi.open(1);


print("Polling the MIDI Device. Press Control-C to exit.")
midi.poll();

