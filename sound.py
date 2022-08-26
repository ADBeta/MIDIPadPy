import simpleaudio as sa

#Array of wave files loaded in to the software.
wave_obj = [None] *64

#Object for playing the audio
play_obj = None

wave_obj[1] = sa.WaveObject.from_wave_file("./kick.wav")
wave_obj[2] = sa.WaveObject.from_wave_file("./snare.wav")
wave_obj[3] = sa.WaveObject.from_wave_file("./cowbell.wav")


def playFromKey(id: int):
	global play_obj, wave_obj

	#If a wave file is playing already, kill it, to start another object
	if play_obj != None:
		if play_obj.is_playing():
			play_obj.stop()

	if wave_obj[id] != None:
		play_obj = wave_obj[id].play()
		
#			global wave_obj, fexe
#					
#			if fexe:
#				play_obj = wave_obj.play()
#				fexe = False
#					
#			#If the play object is playing, kill it
#			if play_obj.is_playing():
#				play_obj.stop()	
#					
#			#Play the audio file now after it was killed, to stop overplay
#			play_obj = wave_obj.play()
