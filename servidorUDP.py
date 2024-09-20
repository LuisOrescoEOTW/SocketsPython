# servidorUDP.py
import socket
import sys
# Validar si se pasaron los argumentos correctos
if len(sys.argv) != 3:
    print("Debe escribir: python servidorUDP.py <server_id> <puerto>")
    sys.exit(1)
# Obtener el ID del servidor y el puerto desde los argumentos
server_id = sys.argv[1]
puerto = int(sys.argv[2])
# Crear el socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Generar una dirección para el servidor
server_address = 'localhost'
# Enlazar el socket a la dirección localhost y al puerto especificado
sock.bind((server_address, puerto))
print(f"Servidor {server_id} escuchando en puerto {puerto}...")
# Ciclo infinito para recibir múltiples mensajes
while True:
    # Recibir el mensaje (máximo 4096 bytes)
    data, address = sock.recvfrom(4096)
    # Mostrar mensaje recibido con el identificador del servidor
    print(f"Servidor {server_id} recibió desde {address} el mensaje: {data.decode()}")
