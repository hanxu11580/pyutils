from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    server = socket(
        family=AF_INET,
        type=SOCK_STREAM
    )
    server.bind(('127.0.0.1',6789))
    server.listen(521)
    print("服务器已启动")
    while True:
        client, addr = server.accept()
        print(f'{addr}连接服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()
        
if __name__ == '__main__':
    main()
    # 测试 telnet 127.0.0.1 6789
    