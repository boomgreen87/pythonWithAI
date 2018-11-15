import pyaudio
import wave


def playaudio(filename):
	chunk = 1024 # Split our audio file up into chunks
	wf = wave.open(filename, 'rb') # Open the audio file as a readable binary stream
	pa = pyaudio.PyAudio() # Instantiate the pyAudio class

	stream = pa.open(
		format=pa.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(), 
		rate=wf.getframerate(),
		output=True
	)

	data_stream = wf.readframes(chunk)

	while data_stream:
		stream.write(data_stream)
		data_stream = wf.readframes(chunk)

	stream.close()
	pa.terminate()


playaudio('./audio/alert1.wav')