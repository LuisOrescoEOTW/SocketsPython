#  Python – Server Datagrama
# Servidor que utiliza sockets para recibir datos del cliente utilizando el protocolo UDP
# (User Datagram Protocol).
import socket
#función socket.socket() - AF_INET: IPv4 - SOCK_DGRAM: protocolo UDP 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#se vincula (bind) el socket a una dirección y puerto
sock.bind(('localhost', 5000))
#Entra en un bucle infinito
while True:
  #Escucha el socket y espera recibir mensajes
    #data: msj en bytes - address: IP y puerto del cliente
    data, address = sock.recvfrom(4096)
    #Imprime: len(data): N° bytes recibidos - address:dirección del cliente - data:mensaje
    print('received {} bytes from {} message {}'.format(len(data), address, data))
