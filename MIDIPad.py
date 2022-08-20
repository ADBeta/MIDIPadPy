#ADBeta 
#20 Aug 2022
#Version 0.5

import midi

#Output light tinkering
#import time
#import rtmidi

#midiout = rtmidi.MidiOut()
#midiout.open_port(1)

#for x in range(0, 127):
#	note_on = [144, x, 1] # Green
#	midiout.send_message(note_on)
#	time.sleep(0.01);

#for x in range(0, 127):
#	note_on = [144, x, 3] # Red
#	midiout.send_message(note_on)
#	time.sleep(0.01);

#for x in range(0, 127):
#	note_on = [144, x, 5] # Yellow
#	midiout.send_message(note_on)
#	time.sleep(0.01);

midi.open(1);
print("Polling the MIDI Device. Press Control-C to exit.")

midi.poll();

