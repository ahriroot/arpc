import asyncio
from arpc.client import new_arpc_conn, new_arpc_conn_async
from arpc_package.api.api import Client, RequestV1


async def main_async():
    conn = await new_arpc_conn_async("127.0.0.1", 9000)
    client = Client(conn)
    request = RequestV1(user_id=1)
    response = await client.get_user_v1(request)
    print(await response.json())


def main():
    conn = new_arpc_conn("127.0.0.1", 9000)
    client = Client(conn)
    request = RequestV1(user_id=1)
    response = client.get_user_v1(request)
    print(response.json())


if __name__ == '__main__':
    # main()
    asyncio.run(main_async())
