
# # cliente.py
import asyncio
import websockets

# # Función para enviar un mensaje al servidor y recibir la respuesta
async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
#         # Enviar un mensaje al servidor
        message = "Hola, servidor soy Luis!"
        await websocket.send(message)
        print(f"Mensaje enviado al servidor: {message}")

#         # Recibir la respuesta del servidor
        response = await websocket.recv()
        print(f"Respuesta recibida del servidor: {response}")

# # Ejecutar la comunicación con el servidor
asyncio.get_event_loop().run_until_complete(communicate())

