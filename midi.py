#ADBeta 
#21 Aug 2022
#Version 0.7

import time
import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()

#Array of button states
MIDIBtnState = [0] * 127

#List all availible MIDI Ports/Devices
def list():
	print("list");

#Open specific port, this is the input and output device
def open(port):
	global midiin, midiout
	
	midiin.open_port(port)
	midiout.open_port(port)
	
	#Verbose print TODO
	#print("MIDI data via port: ", port_name)

#Constantly poll the port for new messages
def poll():
	try:
		timer = time.time()
		while True:
			#Get a MIDI message packet from buffer
			msg = midiin.get_message()
		
			#If the packet has information
			if msg:
				
				#Get the status byte and the 'pitch' byte
				status = int(msg[0][0])
				pitch = int(msg[0][1])
				
				#Set the button at -pitch- to 0 or 1 depending on status
				if status == 144:
					MIDIBtnState[pitch] = 1
					
					#Set the button light to on
					btnLightCall(pitch, 5)
			
				if status == 128:
					MIDIBtnState[pitch] = 0
					
					#Set the button light to off
					btnLightCall(pitch, 0)
					
			#Sleep for some amount of time. Laggy at 0.05 but less CPU
			time.sleep(0.0005)
	except KeyboardInterrupt:
		print('')
	finally:
		close()

#Manage the output lighting based on call 
def btnLightCall(pitch: int, val: int):
	midiout.send_message([144, pitch, val])

#Close and delete the midi devices
def close():
	global midiin, midiout
	print("Exit.")
	
	#Delete midi in
	midiin.close_port()
	del midiin
	
	#Delete midi out
	midiout.close_port()
	del midiout
	
	
