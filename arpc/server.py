import asyncio
from socket import socket, AF_INET, SOCK_STREAM


BUFLEN = 8192


class Server:

    def __init__(self, ip, port, client_count=8):
        self.ip = ip
        self.port = port
        self.client_count = client_count
        self.listenSocket = socket(AF_INET, SOCK_STREAM)
        self.listenSocket.bind((self.ip, self.port))

    async def handle(self, reader, writer):
        addr = writer.get_extra_info('peername')
        while True:
            data = await reader.read(BUFLEN)
            if not data:
                print(f'客户端{addr}关闭了连接')
                writer.close()
                break

            message = data.decode()
            print(f'收到{addr}信息： {message}')

            writer.write(data)

    def start(self):

        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(self.handle, self.ip, self.port, loop=loop)
        server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print(f'Serving on {self.ip}:{self.port}')
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        # Close the server
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
