import socket


if __name__ == '__main__':

    client = socket.socket()

    client.connect(("localhost", 9000))

    while True:
        msg = input(">>:").strip()
        if len(msg) == 0:
            continue
        client.send(msg.encode("utf-8"))

        data = client.recv(1024)
        print("来自服务器:", data)
