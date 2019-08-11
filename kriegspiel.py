import chess
import chess.variant
import os
import socket

clear = lambda: os.system('cls')

def printBoard(board,turn,fog):
    print("  ╔═════════════════╗")
    boardString = "8 ║ "
    line=8
    for i in board.__str__():
        if fog:
            if i=='\n':
                line-=1 
                boardString += ' ║\n' + str(line) +' ║ '
            elif (turn and i>='a' and i<='z'): boardString += '.'
            elif((not turn) and i>='A' and i<='Z'): boardString += '.'
            else: boardString+=i
        else:
            if i=='\n':
                line-=1 
                boardString += ' ║\n' + str(line) +' ║ '
            elif (turn and i>='a' and i<='Z'): boardString += '.'
            else: boardString+=i
    print(boardString+" ║")
    
    print("  ╚═════════════════╝")
    print("    A B C D E F G H")

def Partija(board, krieg):
    clear()
    partijaOn=True
    while partijaOn:
        try:
            clear()    
            input("White plays" if board.turn else "Black plays")
            clear()
            printBoard(board,board.turn, krieg)
            print("Available moves:")
            for i in board.legal_moves:
                print(i.uci())
            potez=input("Move: ")
            for i in board.legal_moves:
                if i.uci()==potez:
                    """and board.piece_at(i.from_square).color==board.turn"""
                    board.push_uci(potez)
                    clear()
                    printBoard(board,not board.turn, krieg)
                    potvrda=input("Confirm?(y/n): ")
                    clear()
                    if(potvrda!="y"):
                        board.pop()
                        clear()
                    else:
                        if board.turn and krieg:
                            clear()
                            potvrda=input("Judge time?(y/n)\n")
                            if(potvrda=="y"):
                                clear()
                                input(board)
                                clear()
                                input("Judge time over")
                    clear()
        except KeyboardInterrupt:
            clear()
            break
            
                
                         

        

        #if board.is_game_over:
        #    print("\n"+str(board.result))
        #    partijaOn=False
        
def TipIgre():
    response=""
    while response!="y":
        ulaz=input("Choose game type (Classic, Atomic, Crazyhouse, Suicide, Giveaway, King of the Hill, Racing Kings, Three-check, Horde):\n")
        if ulaz=="Classic":board = chess.Board()
        elif ulaz=="Atomic":board = chess.variant.AtomicBoard()
        elif ulaz=="Crazyhouse":board = chess.variant.CrazyhouseBoard()
        elif ulaz=="Suicide":board = chess.variant.SuicideBoard()
        elif ulaz=="Giveaway":board = chess.variant.GiveawayBoard()
        elif ulaz=="King of the Hill":board = chess.variant.KingOfTheHillBoard()
        elif ulaz=="Racing Kings":board = chess.variant.RacingKingsBoard()
        elif ulaz=="Three-check":board = chess.variant.ThreeCheckBoard()
        elif ulaz=="Horde":board = chess.variant.HordeBoard()
        else: board = chess.Board()
        print(board)
        response=input("\nThis good?(y/n)\n")
        clear()
        if input("Kriegspiel?(y/n)\n")=='y':
            krieg=True
        else:
            krieg=False
    return board,krieg

while True:
    board,krieg=TipIgre()
    Partija(board,krieg)
    response=input("New Game?(y/n): ")
    if(response!="y"):
        break

    


    
    
