# clienteWS.py
import asyncio
import websockets
import sys
# Validar si se pasaron los argumentos correctos
if len(sys.argv) < 4:
    print("Debe escribir: python clienteWS.py <client_id> <mensaje> <puerto1> <puerto2> ...")
    sys.exit(1)
# Obtener el ID del cliente y el mensaje a enviar
client_id = sys.argv[1]
mensaje = sys.argv[2]
puertos = [int(p) for p in sys.argv[3:]]
# Crear el mensaje completo con el id del cliente
mensaje_completo = f"Hola desde el cliente {client_id}: {mensaje}"
# Función para enviar mensajes a los servidores
async def send_message(puerto):
    uri = f"ws://localhost:{puerto}"
    async with websockets.connect(uri) as websocket:
        await websocket.send(mensaje_completo)
        print(f"Cliente {client_id} envió el mensaje al servidor en el puerto {puerto}")
# Enviar el mensaje a cada uno de los puertos especificados
async def main():
    await asyncio.gather(*(send_message(puerto) for puerto in puertos))
# Ejecutar el envío de mensajes
asyncio.get_event_loop().run_until_complete(main())