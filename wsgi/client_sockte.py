import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 1314))
info = clientsocket.recv(1024)
print(info.decode('utf-8'))