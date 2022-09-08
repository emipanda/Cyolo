import websockets
import asyncio
from rest_api_server import run_flask
from app import extract_words
import threading

PORT = 7890

print("Server listening on Port " + str(PORT))


async def words_server(websocket):
    print("A client just connected")
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            extract_words(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")


async def start_ws_server():
    async with websockets.serve(words_server, "localhost", PORT):
        await asyncio.Future()


def start_servers():
    threading.Thread(target=lambda: run_flask()).start()
    asyncio.run(start_ws_server())


if __name__ == '__main__':
    start_servers()
