#client.py

import socket

server_ip = '192.168.93.130' #อยากติดต่อเครื่องไหน ก็ให้เปลี่ยนเลข IP เครื่องอื่น
port = 5000

while True:
    data = input('Send Message: ')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.connect((server_ip,port))

    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server: ', data_server)
    server.close()