# clienteUDP.py
import socket
import sys
# Validar si se pasaron los argumentos
if len(sys.argv) < 4:
    print("Debe escribir: python clienteUDP.py <client_id> <mensaje> <puerto1> <puerto2> ...")
    sys.exit(1)
# Obtener el ID del cliente y el mensaje a enviar
client_id = sys.argv[1]
mensaje = sys.argv[2]
puertos = [int(p) for p in sys.argv[3:]]
# Crear el mensaje completo con el ID del cliente
mensaje_completo = f"Hola desde el cliente {client_id}: {mensaje}".encode()
# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Dirección del servidor (localhost)
server_address = 'localhost'
# Enviar el mensaje a cada uno de los puertos especificados
for puerto in puertos:
    # Enviar el mensaje al servidor en el puerto actual
    sent = sock.sendto(mensaje_completo, (server_address, puerto))
    print(f"Cliente {client_id} envió el mensaje al servidor en el puerto {puerto}")
