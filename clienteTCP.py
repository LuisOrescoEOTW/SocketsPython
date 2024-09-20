# clienteTCP.py
import socket
import sys
# Validar si se pasaron los argumentos correctos
if len(sys.argv) < 4:
    print("Debe escribir: python clienteTCP.py <client_id> <mensaje> <puerto1> <puerto2> ...")
    sys.exit(1)
# Obtener el ID del cliente y el mensaje a enviar
client_id = sys.argv[1]
mensaje = sys.argv[2]
puertos = [int(p) for p in sys.argv[3:]]
# Dirección del servidor (localhost)
server_address = 'localhost'
# Crear el mensaje completo con el ID del cliente
mensaje_completo = f"Hola desde el cliente {client_id}: {mensaje}".encode()
# Enviar el mensaje a cada uno de los puertos especificados
for puerto in puertos:
    # Crear el socket TCP (cambio de SOCK_DGRAM a SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectar al servidor en el puerto especificado
    sock.connect((server_address, puerto))
    try:
        # Enviar el mensaje
        sock.sendall(mensaje_completo)
        print(f"Cliente {client_id} envió el mensaje al servidor en el puerto {puerto}")
    finally:
        # Cerrar el socket
        sock.close()
