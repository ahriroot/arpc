import asyncio
import socket


async def task1():
    while True:
        print('hello')
        await asyncio.sleep(1)


async def task2():
    while True:
        print('world')
        await asyncio.sleep(1)


async def handle(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data)
        client_socket.send(data)
    client_socket.close()


async def run():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_socket.bind(('127.0.0.1', 8080))
    tcp_socket.listen(128)
    print('Serving')
    while True:
        client_socket, _ = tcp_socket.accept()
        asyncio.create_task(handle(client_socket))


async def main():
    await run()


if __name__ == '__main__':
    asyncio.run(main())
