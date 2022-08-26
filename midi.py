import rtmidi

# MIDI Variables ###############################################################
#MIDI input/output devices, force ALSA API
midiout = rtmidi.MidiOut(rtapi=rtmidi.API_LINUX_ALSA)
midiin = rtmidi.MidiIn(rtapi=rtmidi.API_LINUX_ALSA)

#Key input event variables
class EventKeyIn:
	s = 0 #Status
	p = 0 #Pitch
	v = 0 #Velocity

# Functions ####################################################################
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
	
	print("MIDI data via port: ", midiin.get_port_name)

#Poll the MIDI Device for events. Return codes:
#	0	No change
#	1	Key Event
#	2	Control Event TODO
def poll():
	#Get a MIDI message packet from buffer
	msg = midiin.get_message()
			
	#If the packet has information
	if msg:
		#Get the status, pitch and velocity, pass to key in event class
		#TODO add cntrl vs key detection and var setting
		EventKeyIn.s = int(msg[0][0])
		EventKeyIn.p = int(msg[0][1])
		EventKeyIn.v = int(msg[0][2])
		
		return 1
	
	#Else return 0 for no action
	else:
		return 0
		
#Send 3 ints as a message to the MIDI device
def send(s: int, p: int, v: int):
	midiout.send_message([s, p, v])
	

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
