import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connecting...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection form %s:%s closed' % addr)


while True:
    sock,addr = s.accept()  # 接收客户端的连接和地址
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 创建新线程来处理TCP连接
    t.start()