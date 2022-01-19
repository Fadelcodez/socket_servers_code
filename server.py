import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

while True:
  clientSocket, address = server.accept()
  if SERVER in address:
    print('Host Connection Established :D')
   else:
    print(f'Anonymous Connection detected: {address}')
  clientSocket.close()
  
