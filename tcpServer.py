import socket
from threading import Thread
import json
from commandHandler import handleCommand

tcpSrv = None

def setTCPServer(server):
    global tcpSrv
    tcpSrv = server

def getTCPServer():
    global tcpSrv
    return tcpSrv

class tcpServer:
    def __init__(self, host, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self._socket.bind((host, port))
        print('listening')
        self._socket.listen(1)

        self.conn = self._socket.accept()[0]
        print('client connected')
        self.thread = Thread(target=self.listener)
        self.thread.start()

    def listener(self):
        while(True):
            data = self.conn.recv(2048)
            if data != None and len(data) > 0:
                data = data.decode('utf-8')
                try:
                    data = json.loads(data)
                except: 
                    continue
                packetId = data['packetId']
                _data = data['data']

                if packetId == 0:
                    cmd = _data
                    handleCommand(cmd)

    def sendMessage(self, packetId, data):
        if (hasattr(self, 'conn')):
            try:
                json = {
                    'packetId': packetId,
                    'data': data
                }
                self.conn.send(str(json).encode())
            except Exception as err:
                print('tcpServer sendMessage: ' + err)

    def sendSensorData(self, sensorId, sensorData):
        data = {
            "sensor": sensorId,
            "data": sensorData
        }

        self.sendMessage(1, data)
