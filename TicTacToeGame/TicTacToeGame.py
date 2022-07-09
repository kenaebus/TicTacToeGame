#Tic Tac Toe Game
# Inspiration for idea is from "Tech with Tim" on Youtube

board = [' ' for x in range(10)]

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print('   |   |')
    pass

def isFreeSpace(pos):
    return  board[pos] == ' '
   

def isBoardFull(board):
    count = board.count(' ')

    if count == 9:
        return True
    else:
        return False

def compMove():
    # Check for all possible moves

    import random
    computer = randint(1,9)
    pass

def playerMove(player):
    # Check for valid move by user - validate
    pass

def insertLetter(letter, pos):
    board[pos] = letter;

def isWinner(board, letter):


    return ((board[1] == letter and board[2] == letter and board[3] == letter) or    # Horizontal top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # Horizontal Middle
    (board[7] == letter and board[8] == letter and board[9] == letter) or # Horizontal Bottom
    (board[1] == letter and board[4] == letter and board[7] == letter) or # Vertical Left
    (board[2] == letter and board[5] == letter and board[8] == letter) or # Vertical Middle
    (board[3] == letter and board[6] == letter and board[9] == letter) or # Vertical Right
    (board[1] == letter and board[5] == letter and board[9] == letter) or # Diagonal Right to Left
    (board[3] == letter and board[5] == letter and board[7] == letter))   # Diagonal Left to Right
    pass

def main():
    # Main Loop

    print("Welcome to Tic Tac Toe! Type in a number between 1-9 to place an 'X' on the board \n")
    printBoard(board)

    while not isBoardFull(board):
      if not isWinner(board,'X'):

      else:    
          print("Win")
          break;

      if not isWinner(board, 'O'):

      else:
          print("Lose")
          break;

    if isBoardFull(board):
        print("Tied! Board is filled up!")
        break;

main()
