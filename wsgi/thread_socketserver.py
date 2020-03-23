import errno
import socket
import threading
import time


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''
Hello World! <h1> from the5fire 《Django 企业开发实践》</h1> -from{thread_name}
'''

response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 27 may 2018 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Lenght: {lenght}\r\n',
    body,
]

response = '\r\n'.join(response_params)

def handle_connection(conn, addr):
    # print(conn, addr)
    # time.sleep(10)
    request = b''
    # 设置为非阻塞模式是这里会报错
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)

    print(request)
    current_thread = threading.currentThread()
    content_lenght = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)
    conn.send(response.format(thread_name=current_thread.name, lenght=content_lenght).encode())
    conn.close()

def main():
    # socket.AF_INET用于服务器与服务器之间的通信
    # socket.SOCK_STREAM用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用,保证我们每次按ctrl+c组合键之后,快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)
    print('http://127.0.0.1:8000')
    serversocket.setblocking(0) # 设置socket为非阻塞模式

    try:
        i = 0
        while True:
            try:
                conn, address = serversocket.accept()
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s'% i)
            t.start()
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()
