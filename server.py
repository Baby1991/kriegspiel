from threading import Thread
import socket
import sys

PORT = len(sys.argv) > 1 and sys.argv[1] or 65432
threads = []

def connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            continue
        print(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        thread = Thread(target=connection, args=(conn, addr))
        threads.append(thread)
        thread.start()
