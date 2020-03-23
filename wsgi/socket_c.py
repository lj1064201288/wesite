import socket


socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketclient.connect(('127.0.0.1', 1314))
info = socketclient.recv(1024)
print(info.decode('utf-8'))