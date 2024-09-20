# servidorTCP.py
import socket
import sys
# Validar si se pasaron los argumentos correctos
if len(sys.argv) != 3:
    print("Debe escribir: python servidorTCP.py <server_id> <puerto>")
    sys.exit(1)
# Obtener el ID del servidor y el puerto desde los argumentos
server_id = sys.argv[1]
puerto = int(sys.argv[2])
# Generar una dirección para el servidor
server_address = 'localhost'
# Crear el socket TCP (cambio de SOCK_DGRAM a SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlazar el socket a la dirección y al puerto especificado
sock.bind((server_address, puerto))
# Poner el socket en modo de escucha para aceptar conexiones
sock.listen(5)  # Permite hasta 5 conexiones pendientes
print(f"Servidor {server_id} escuchando en puerto {puerto}...")
# Ciclo infinito para aceptar múltiples conexiones y recibir mensajes
while True:
    # Aceptar la conexión entrante
    connection, client_address = sock.accept()
    try:
        print(f"Conexión establecida con {client_address}")
        # Recibir el mensaje (máximo 4096 bytes)
        data = connection.recv(4096)
        if data:
            # Mostrar el mensaje recibido
            print(f"Servidor {server_id} recibió desde {client_address} el mensaje: {data.decode()}")
        else:
            print(f"Conexión cerrada por {client_address}")
    finally:
        # Cerrar la conexión
        connection.close()
