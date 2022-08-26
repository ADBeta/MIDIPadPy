#ADBeta

import rtmidi
import sound

#MIDI input/output devices, force ALSA API
midiout = rtmidi.MidiOut(rtapi=rtmidi.API_LINUX_ALSA)
midiin = rtmidi.MidiIn(rtapi=rtmidi.API_LINUX_ALSA)

#List all availible MIDI Ports/Devices
def list():
	ports = midiout.get_ports()
	print("ports: ")
	print(ports);

#Open specific port, this is the input and output device
def open(port):
	global midiin, midiout
	
	midiin.open_port(port)
	midiout.open_port(port)
	
	#Verbose print TODO
	print("MIDI data via port: ", midiin.get_port_name)

#Constantly poll the port for new messages
def poll():
	#Get a MIDI message packet from buffer
	msg = midiin.get_message()
			
	#If the packet has information
	if msg:
		#Get the status byte and the 'pitch' byte
		status = int(msg[0][0])
		pitch = int(msg[0][1])
		velocity = int(msg[0][2])
				
		if status == 144 or status == 128:
			#Send button data to function for handling
			MIDIKey(status, pitch, velocity)
		
		#TODO Add control/slider handler
			
					
#Handle a MIDI key press, status, pitch, velocity.
def MIDIKey(s: int, p: int, v: int):
	#TODO If midiout is enabled
	#If Keys is pressed, send lighting on signal
	if s == 144:
		midiout.send_message([144, p, 5])
		sound.playFromKey(p)
	
	#If key is released, send lighting off signal
	if s == 128:
		midiout.send_message([144, p, 0])
	
	
					
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
	
	
