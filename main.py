from arpc.utils import main

from arpc.server import Server

from arpc_package.api.api import Arpc, RequestV1, ResponseV1


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
    main()
    # start()
