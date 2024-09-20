# Python – Client Datagrama
# Cliente que utiliza sockets para enviar datos al servidor utilizando el protocolo UDP
# (User Datagram Protocol).

import socket

#función socket.socket() - AF_INET: IPv4 - SOCK_DGRAM: protocolo UDP 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#'localhost': máquina local (loopback) - 10000: puerto que está escuchando mensajes UDP
server_address = ('localhost', 5000)
# mensaje codificado como bytes: b
message = b'Lorem ipsum dolor sit amet, consectetur.'
#Muestra por console el mensaje enviado
print('sending {!r}'.format(message))
#sock.sendto(): envía el mensaje al servidor. Dos argumentos: message: mensaje. 
  #server_adress: La dirección y el puerto del servidor.
sent = sock.sendto(message, server_address)
