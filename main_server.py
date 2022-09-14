from concurrent.futures import ThreadPoolExecutor
from rest_api_server import run_flask
from app import extract_words
import websockets
import threading
import asyncio


PORT = 7890

print("Server listening on Port " + str(PORT))

executor = ThreadPoolExecutor()


async def words_server_listener(websocket):

    print("A client just connected")
    with ThreadPoolExecutor() as pool:
        tasks = []
        loop = asyncio.get_running_loop()
        try:
            async for message in websocket:
                tasks.append(
                    loop.run_in_executor(pool, extract_words, message)
                )
                for task in asyncio.as_completed(tasks):
                    await task

        except websockets.exceptions.ConnectionClosed as e:
            print("A client just disconnected")


async def start_ws_server():
    async with websockets.serve(words_server_listener, "localhost", PORT):
        await asyncio.Future()


def start_servers():
    threading.Thread(target=lambda: run_flask()).start()
    asyncio.run(start_ws_server())


if __name__ == '__main__':
    start_servers()
