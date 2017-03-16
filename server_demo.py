# coding:utf-8
from socket import *
__doc__ = """
用socket实现简单server
"""

Port = 12306
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', Port))
serverSocket.listen(5)
while True:
    print 'Ready to server...'
    connect, addr = serverSocket.accept()
    try:
        message = connect.recv(1024)
        filename = message.split()[1]
        print filename
        f = open(filename[1:])
        output_data = f.read()
        f.close()
        connect.send('HTTP/1.0 200 OK\r\n\r\n')
        for i in range(0, len(output_data)):
            connect.send(output_data[i])
        connect.close()
    except IOError:
        connect.send('404 Not Found')
        connect.close()
serverSocket.close()
