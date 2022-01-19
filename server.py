import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

while True:
  clientSocket, address = server.accept()
  print(f'Server Connection Established :D: {address}')
  clientSocket.close()
  
