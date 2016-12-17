import socket

host = "192.168.10.3"
port = 3002

serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversock.bind((host,port))

while True:
    data, (addr, port) = serversock.recvfrom(1024)
    print data
serversock.close()
