#Server.py

import socket

my_ip = '192.168.93.130'
port = 5000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((my_ip,port))
    server.listen(1)

    print('waiting for client...')

    client, addr = server.accept()
    print('Connect from: ', str(addr))

    data = client.recv(1024).decode('utf-8')
    print('Message from Client: ', data)

    #resp_text = 'We received'
    if data == '500':
        resp_text = 'FUCK U SORWOR SUS PRAYUTH'
    elif data == '250':
        resp_text = 'Welcome ANACOTMAI'
    else:
        resp_text = 'What is your TEAM?'

    client.send(resp_text.encode('utf-8'))
    client.close()