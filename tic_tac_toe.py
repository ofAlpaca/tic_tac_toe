import random
import time

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ' ';
    while not (letter == 'X' or letter == 'O'):
        print('Do you want 2 be X or O')
        letter = input()
    if letter == 'X':
        return ['X','O']
    else :
        return ['O','X']

def whoGoseFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Play again ? (y)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isSpaceFree(board, move):
    return board[move] == ' '
"""
def isWinner(bo, le, n):
    #find column
    for i in range(1,n+1):
        count = 0
        for j in range(0,n):
            if bo[n*j+i] == le:
               count = count + 1
        if count == n:
            return True
    #find row
    for i in range(1,n*n-n+2,n):
        count = 0
        for j in range(0,n):
            if bo[i+j] == le:
               count = count + 1
        if count == n:
            return True
    #find cross
    count = 0
    for i in range(0,n*n,n+1):
        if bo[1+i] == le:
            count = count + 1
    if count == 4:
        return True

    count = 0
    for i in range(0,n*n-n+1,n-1):
        if bo[n+i] == le:
            count = count + 1
    if count == 4:
        return True
"""

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
      (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
      (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
      (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
      (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
      (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
      (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
      (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getPlayerMove(board):
    move = ' '
    #'1 2 3 4 5 6 7 8 9'.split()
    while move not in ['1','2','3','4','5','6','7','8','9'] or not isSpaceFree(board, int(move)):
        print('What is your next? (1-9)')
        move = input()
    return int(move)

def choseRandomMoveFromList(board, movelist):
    possibleMoves = []
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
        
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

def copyBoard(board):
    copyboard = []
    for i in board:
        copyboard.append(i)
    return copyboard

def getComMove(board, computerletter):
    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

    # if computer's next move can win
    for i in range(1,10):
        copy = copyBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy,computerletter,i)
            if isWinner(copy,computerletter):
                return i

    # if player's next move can win
    for i in range(1,10):
        copy = copyBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy,playerletter,i)
            if isWinner(copy, playerletter):
                return i

    move = choseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    if isSpaceFree(board,5):
        return 5

    return choseRandomMoveFromList(board, [2,4,6,8])

print('## Welcome to Tic Tac Toe! ##')

while True:
    theBoard = [' '] * 10
    playerletter, computerletter = inputPlayerLetter()
    turn = whoGoseFirst()
    print('## ' + turn + ' will go first! ##')
    gameIsPlaying = True

    while gameIsPlaying :
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerletter,move)

            if isWinner(theBoard, playerletter):
                drawBoard(theBoard)
                print('## You win the game! ##')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('## The game is tie! ##')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComMove(theBoard,computerletter)
            makeMove(theBoard,computerletter,move)

            if isWinner(theBoard, computerletter):
                drawBoard(theBoard)
                print('## You were defeated by computer! ##')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('## The game is tie! ##')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        print('## Thank you for playing! ##')
        time.sleep(3)
        break

