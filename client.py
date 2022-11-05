import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() # Ip del host
port = 444

clientsocket.connect((host, port))

message = clientsocket.recv(1024) # Cantidad máixma de bytes que se puede recibir en el puerto

clientsocket.close()

print(message.decode('ascii'))