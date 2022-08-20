#ADBeta 
#20 Aug 2022
#Version 0.5

import time

#Midi open functionality
from rtmidi.midiutil import open_midiinput

#Array of buttons
MIDIBtn = [0] * 127


#List all availible MIDI Ports/Devices
def list():
	print("list");

#Open specific port to be used as the input device
def open(port):
	global g_midiin
	
	g_midiin, port_name = open_midiinput(port)
	#Verbose print
	print("MIDI data via port: ", port_name)

#Constantly poll the port for new messages
def poll():
	try:
		timer = time.time()
		while True:
			#Get a MIDI message packet from buffer
			msg = g_midiin.get_message()
		
			#If the packet has information
			if msg:
				#Get the status byte and the 'pitch' byte
				status = msg[0][0]
				pitch = msg[0][1]
				
				if status == 144:
					MIDIBtn[pitch] = 1
				
				if status == 128:
					MIDIBtn[pitch] = 0
				
				
				#print(msg[0])
				print(MIDIBtn)

			time.sleep(0.005)
	except KeyboardInterrupt:
		print('')
	finally:
		close()

#Close and delete the midi in device
def close():
	global g_midiin

	print("Exit.")
	g_midiin.close_port()
	del g_midiin
