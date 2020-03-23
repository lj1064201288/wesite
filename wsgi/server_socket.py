import socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 1314))
serversocket.listen(2)
q, v = serversocket.accept()
q.send(b'Hello World!')