import chess
import socket
import sys

HOST = len(sys.argv) > 1 and sys.argv[1] or '127.0.0.1'
PORT = len(sys.argv) > 2 and sys.argv[2] or 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b'hmm')
    sock.close()
