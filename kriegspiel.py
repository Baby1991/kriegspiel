import chess
import os
import socket
board = chess.Board()
clear = lambda: os.system('cls')

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
    
       
while True:
    Partija()
    response=input("New Game?(y/n): ")

    


    
    