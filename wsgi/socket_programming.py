import socket


ip = socket.gethostbyname('augs')
name = socket.gethostname()
baidu = socket.gethostbyname('www.baidu.com')

wangyi_ex = socket.gethostbyname_ex('www.163.com')
youdao = socket.gethostbyaddr('202.165.102.205')
server_name = socket.getservbyname('http', 'tcp')
server_telnet = socket.getservbyname('telnet', 'tcp')
print(baidu)