import cv2
import socket
import pickle

def initImgClient():
    print("connecting")
    s = socket.socket()
    #s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,1000000)

    server_ip = "127.0.0.1"
    server_port = 7777

    s.connect((server_ip,server_port))
    print("connected")


    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while cap.isOpened():
        ret, img = cap.read()
    
        cv2.imshow('Img Client', img)
    
        ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY),30])
    
        x_as_bytes = pickle.dumps(buffer)
        
        s.sendto((x_as_bytes),(server_ip,server_port))
    
        if cv2.waitKey(5) & 0xFF == 27:
            break


    cv2.destroyAllWindows()
    cap.release()