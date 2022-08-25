#ADBeta

import rtmidi

#MIDI input/output devices, force ALSA API
midiout = rtmidi.MidiOut(rtapi=rtmidi.API_LINUX_ALSA)
midiin = rtmidi.MidiIn(rtapi=rtmidi.API_LINUX_ALSA)

#Array of button states
MIDIBtnState = [0] * 127

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
				
		#Set the button at -pitch- to 0 or 1 depending on status
		if status == 144:
			MIDIBtnState[pitch] = 1
			#Set the button light to on
			btnLightCall(pitch, 5)
			
		if status == 128:
			MIDIBtnState[pitch] = 0		
			#Set the button light to off
			btnLightCall(pitch, 0)
					
					
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
	
	
