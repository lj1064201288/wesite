import time
import socket

socketcilent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketcilent.connect(('127.0.0.1', 1315))
data = socketcilent.recv(1024)
socketcilent.send(b'hello,1')
print(data)
time.sleep(50)