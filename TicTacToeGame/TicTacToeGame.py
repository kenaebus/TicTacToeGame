#Tic Tac Toe Game

# Create board list with 9 spaces
board = [' ' for x in range(10)]

# Print board in tic-tac-toe format
# Set the list from 1-9 on the board to be modified throughout the program
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

# Checks if the space is empy - Returns boolean
def isFreeSpace(pos):
    return  board[pos] == ' '
   
# Checks if the board is full by counting the amount of empty spaces (if applicable) - Returns boolean
def isBoardFull(board):
    count = board.count(' ')

    if count == 9:
        return True
    else:
        return False

def selectRandom():
    pass

def compMove():
    # Check for all possible moves
   possibleMoves = []


    # Will check if corners are open
     

def playerMove():
    # Check for valid move by user - validate
    run = True # Run till there is possible move
    while not run:
        move = input("Select number from 1- 9 to place an 'X' on the board")
        try:
            move = int(input) # Turn move into a int
            if (move > 0 or move < 10):
                if isFreeSpace(pos):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry this place is taken")
            else:
                print("Please choose a valid number")
        except:
            print("Please enter a number!")
    pass

# Replaces current list element with letter
def insertLetter(letter, pos):
    board[pos] = letter;

# Checks if letter (X or O) have valid patterns
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
          compMove()
          if (compMove() == 0):
              print("No more spaces")
              break
          else:
              insertLetter('O', compMove())
              print('Computer placed an \'O\' in position', move , ':')
              printBoard(board)
      else:    
          print("Win")
          break;

      if not isWinner(board, 'O'):
          playerMove()
          printBoard(board)
      else:
          print("Lose")
          break;

    if isBoardFull(board):
        print("Tied! Board is filled up!")

while True:
    answer = input("Would you like to play again? y/n")
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        board = [' ' for x in range(10)]
        print("-------------------------")
        main()
    else:
        break
