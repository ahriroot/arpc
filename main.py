from arpc import run, Server


if __name__ == '__main__':
    # run('api.arpc')
    server = Server(ip='127.0.0.1', port=8080)
    server.start()
