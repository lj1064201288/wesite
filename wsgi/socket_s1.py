import socket


while True:
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socketserver.bind(('127.0.0.1', 1315))
    socketserver.listen(10)
    q, v = socketserver.accept()
    q.send(b'Come and you love me')
    print(q.recv(1024))
    q.close()