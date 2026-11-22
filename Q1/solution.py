import socket, struct, threading

def send_msg(sock, text):
    data = text.encode('utf-8')
    sock.sendall(struct.pack('!I', len(data)) + data)

def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk: raise ConnectionError('closed')
        data += chunk
    return data

def recv_msg(sock):
    (n,) = struct.unpack('!I', recv_exact(sock, 4))
    return recv_exact(sock, n).decode()

def server(listener):
    conn, _ = listener.accept()
    with conn:
        for _ in range(3): print('server got:', recv_msg(conn))
        send_msg(conn, 'all 3 received')

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('127.0.0.1', 0)); listener.listen(1)
th = threading.Thread(target=server, args=(listener,)); th.start()
client = socket.create_connection(listener.getsockname())
for text in ('roll 101 present', 'roll 102 present', 'roll 103 absent'): send_msg(client, text)
print('client got:', recv_msg(client))
client.close(); th.join(); listener.close()
