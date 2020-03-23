import socket

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketserver.bind(('127.0.0.1', 1314))
socketserver.listen(2)
q, v = socketserver.accept()
q.send(b'Hello World')