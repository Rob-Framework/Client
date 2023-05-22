import json
import cv2
import socket
import pickle
from envReader import getValue
from mainLoop import Loop

def initImgClient():
    print("connecting")
    s = socket.socket()

    server_ip = getValue("IP")
    server_port = int(getValue("PORT"))

    s.connect((server_ip,server_port))
    print("connected")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        ret, img = cap.read()
    
        cv2.imshow('Img Client', img)
    
        ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY),30])
    
        x_as_bytes = pickle.dumps(buffer)
        
        s.sendto((x_as_bytes),(server_ip,server_port))

        Loop()

        if cv2.waitKey(5) & 0xFF == 27:
            break


    cv2.destroyAllWindows()
    cap.release()