import socket
from drivers.AudioDriver import get_audio_input
from envReader import getValue
 
connection = None
 
def initAudioSender():
    global connection
    server_ip = getValue("AUDIO_IP")
    server_port = int(getValue("AUDIO_PORT"))
 
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((server_ip, server_port))
 
def audioSenderLoop():
    stream, audio = get_audio_input()
    global connection
    audio_data = stream.read(1024)
    #connection.sendall(audio_data)
 
def Clear():
    global connection
    connection.close()