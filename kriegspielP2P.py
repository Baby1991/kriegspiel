import chess
import os
import socket

clear = lambda: os.system('cls')

def host(ip,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((ip,port))
        sock.listen()
        while True:
            try:
                conn, addr = sock.accept()
                return(conn,addr)
            except KeyboardInterrupt:
                exit()
                
def connect(ip,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        return sock
        
        

def printBoard(turn):
    boardString = ""
    for i in board.__str__():
        if (turn and i>='a' and i<='z'): boardString += '.'
        elif((not turn) and i>='A' and i<='Z'): boardString += '.'
        else: boardString+=i 
    print(boardString)

def Partija():
    partijaOn=True
    while partijaOn:
        clear()
        input("White plays" if board.turn else "Black plays")
        #clear()
        printBoard(board.turn)
        print("Available moves:")
        for i in board.legal_moves:
            print(i.uci())
        potez=input("Move: ")
        for i in board.legal_moves:
            if i.uci()==potez and board.piece_at(i.from_square).color==board.turn:
                board.push_uci(potez)
                clear()
                printBoard(not board.turn)
                potvrda=input("Confirm?(y/n): ")
                if(potvrda!="y"): board.pop()
            
        if not board.is_game_over:
            print("\n"+str(board.result))
            partijaOn=False

HOST = '127.0.0.1'
PORT = 65432
response=input("Host/Join?\n")

if response=="Host":
    konekcija,adresa=host(HOST,PORT)
else:
    soket=host(HOST,PORT)



    
