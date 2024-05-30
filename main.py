def resetgame():
    global board, currentPlayer, winner, gamerunning
    board = ['-','-','-',
             '-','-','-',
             '-','-','-']
    currentPlayer = 'x'
    winner = None
    gamerunning = True


#print Board
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-------')
    print(board[6] + '|' + board[7] + '|' + board[8])

#take player input
def Playerinp(board):
    inp= int(input("choose a number between 1-9: "))
    if inp >=1 and inp <=9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('oops!, the spot is laready taken!')

#check for wins or ties
def checkwin(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    elif board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gamerunning
    if '-' not in board:
        printBoard(board)
        print('it is a Tie!')
        gamerunning = False

#switch player
def switchplayer():
    global currentPlayer
    if currentPlayer == 'x':
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'

#rplay game
while True:
    resetgame()
    while gamerunning:
        printBoard(board)
        Playerinp(board)
        if checkwin(board):
            print(f'the winner is {winner}')
            gamerunning = False
        else:
            checkTie(board)
            switchplayer()
    player_again = input('do you want to play again y/n: ').lower()
    if player_again != 'y':
        break
