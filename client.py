import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.accept((HOST, PORT))
print('Connection established with server :D!')
