import time

#Midi open functionality
from rtmidi.midiutil import open_midiinput

#Dataclass for MIDI messages
class MidiData:
	status = False
	button = 0
	velocity = 0
	
cMsg = MidiData 

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
				statusStr = msg[0][0]
				buttonStr = msg[0][1]
				velocityStr = msg[0][2]
				
				#Set the class variables based on the string
				if statusStr == 144:
					cMsg.status = True
				if statusStr == 128:
					cMsg.status = False
				
				cMsg.button = int(buttonStr)
				cMsg.velocity = int(velocityStr)
				
				
				#Set a variable to just the packet bytes from the MIDI message
				print(cMsg.status, cMsg.button, cMsg.velocity)
				
				
				#message = msg
				#print("[%s]" % (message))

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
