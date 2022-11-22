import asyncio
from arpc.server import Server, ServerAsync

from arpc_package.api.api import Arpc, RequestV1, ResponseV1


class SAsync(Arpc):

    async def get_user_v1(self, request: RequestV1) -> ResponseV1:
        print(request)
        return ResponseV1(user_id=1, username='arpc name async')

    async def post_user_v1(self, request: ResponseV1) -> RequestV1:
        print(request)
        return RequestV1(user_id=1)


async def start_async():

    s = ServerAsync('127.0.0.1', 9000)

    c = SAsync()
    await c.register(s)

    await s.start()


class S(Arpc):

    def get_user_v1(self, request: RequestV1) -> ResponseV1:
        print(request)
        return ResponseV1(user_id=1, username='arpc name')

    def post_user_v1(self, request: ResponseV1) -> RequestV1:
        print(request)
        return RequestV1(user_id=1)


def start():

    s = Server('127.0.0.1', 9000)

    c = S()
    c.register(s)

    s.start()


if __name__ == '__main__':
    # start()
    asyncio.run(start_async())
