import pyaudio

#Based on https://github.com/UniversalMachina/Receive-byte-stream-audio-file-through-microphone
def get_audio_input():
    audio_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    return stream, audio