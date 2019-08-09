from commands import Command
from threading import Thread
import socket
import sys

PORT = len(sys.argv) > 1 and sys.argv[1] or 65432
threads = []

def handle_command(cmd):
    pass

def connection(conn, addr):
    print('New socket:', addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                # Connection closed.
                break
            handle_command(data.decode('utf-8'))
        except OSError:
            # Connection closed.
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', PORT))
    sock.listen()
    while True:
        try:
            conn, addr = sock.accept()
            with conn:
                thread = Thread(target=connection, args=(conn, addr))
                threads.append(thread)
                thread.start()
        except KeyboardInterrupt:
            print('\u001B[1KExiting...')
            break
