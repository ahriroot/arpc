import asyncio
import socket
import threading


BUFLEN = 1024


class ServerAsync:

    def __init__(self, ip, port, client_count=8):
        self.handler = {}
        self.ip = ip
        self.port = port
        self.backlog = 128
        self.client_count = client_count

    def register(self, name, func):
        self.handler[name] = func

    async def accept(self, reader, writer):
        length = 0
        name = ''
        body = b''

        buf = await reader.read(BUFLEN)

        if length == 0:
            res = buf.split(b'\n')
            if len(res) > 2:
                length = int(res[0])
                name = res[1].decode()
                body = res[2]
            else:
                pass

        function = self.handler.get(name)
        if not function:
            print(f'not found handler {name}')
            writer.close()
            return

        res = await function(body, '')
        res = res.serialize()

        data = b''
        data += str(len(res)).encode()
        data += b'\n'
        data += name.encode()
        data += b'\n'
        data += res

        writer.write(data)
        await writer.drain()
        writer.close()

    def _start(self):
        # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # tcp_socket.bind(('127.0.0.1', 9000))
        # tcp_socket.listen(128)
        # print('Serving')
        # while True:
        #     client_socket, _ = tcp_socket.accept()
        #     asyncio.create_task(self.accept(client_socket))

        loop = asyncio.get_event_loop()

        coro = asyncio.start_server(self.accept, '127.0.0.1', 9000)
        server = loop.run_until_complete(coro)

        # Serve requests until Ctrl+C is pressed
        print('Serving on {}'.format(server.sockets[0].getsockname()))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        # Close the server
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()

    def start(self):
        # asyncio.run()
        self._start()
