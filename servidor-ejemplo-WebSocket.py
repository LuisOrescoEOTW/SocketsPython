# # servidor.py
import asyncio
import websockets

# # Función que maneja los mensajes del cliente
async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensaje recibido del cliente: {message}")
        await websocket.send(f"Echo: {message}")

# # Iniciar el servidor WebSocket en localhost en el puerto 8765
start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("Servidor WebSocket iniciado en ws://localhost:8765")
asyncio.get_event_loop().run_forever()
