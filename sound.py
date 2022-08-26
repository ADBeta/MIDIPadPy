import simpleaudio as sa

import lighting #Set idle and pressed key colours

# Sound playing mode settings ##################################################
class SoundMode: #TODO this is weird and messy
	continuous = True
	single = False
	hold = False

# Wave file varibales ##########################################################
#Array of wave files loaded in to the software.
wave_obj = [None] *127

#Object for playing the audio
play_obj = None

# Functions ####################################################################

def loadWave(index: int, filename):
	wave_obj[index] = sa.WaveObject.from_wave_file(filename)
	#TODO If output is enabled, set the idle colour to show an active key
	lighting.idleKeyColour[index] = 1

#Play the wave file loaded in at index id, state 1 = pressed | 0 = released
def playFromKey(status: int, id: int):
	global play_obj, wave_obj
	
	# Mode Detection #
	#Play a single sound at a time, killing any sound that is going before it
	#if SoundMode.single:
		#If a wave file is playing already, kill it, to start another object
	#	if play_obj != None:
	#		if play_obj.is_playing():
	#			play_obj.stop()

	#	if wave_obj[id] != None:
	#		play_obj = wave_obj[id].play()
	
	if SoundMode.continuous:
		if wave_obj[id] != None:
			if status == 144:
				play_obj = wave_obj[id].play()

