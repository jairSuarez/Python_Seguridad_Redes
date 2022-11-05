import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() # Ip del host
port = 444

serversocket.bind((host, port))

serversocket.listen(3) # Máximo numero de peticiones a atender

while True:
    clientsocket, address = serversocket.accept() #aceptar la información TCP proveniente del cliente
    print("Conexión recibida de " + str(address))
    message = 'Hola, gracias por conectarte al servidor!' + "\r\n"
    clientsocket.send(message.encode('ascii')) # Mensaje para el cliente cuando se conexte exitosamente
    clientsocket.close()

