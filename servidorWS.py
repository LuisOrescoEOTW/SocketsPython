# servidorWS.py
import asyncio
import websockets
import sys
# Validar si se pasaron los argumentos correctos
if len(sys.argv) != 3:
    print("Debe escribir: python servidorWS.py <server_id> <puerto>")
    sys.exit(1)
# Obtener el ID del servidor y el puerto desde los argumentos
server_id = sys.argv[1]
puerto = int(sys.argv[2])
# Generar una dirección para el servidor
server_address = 'localhost'
# Función para manejar las conexiones entrantes y mensajes
async def handle_connection(websocket, path):
    print(f"Servidor {server_id} conectado con {path}")
    async for message in websocket:
        print(f"Servidor {server_id} recibió el mensaje: {message}")
# Para configurar el servidor WebSocket
start_server = websockets.serve(handle_connection, server_address, puerto)
# Iniciar el servidor
asyncio.get_event_loop().run_until_complete(start_server)
print(f"Servidor {server_id} escuchando en puerto {puerto}...")
# Mantener el servidor corriendo
asyncio.get_event_loop().run_forever()
