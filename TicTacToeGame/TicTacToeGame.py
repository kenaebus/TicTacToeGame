#Tic Tac Toe Game

# Create board list with 9 spaces
board = [' ' for x in range(10)]


# Replaces current list element with letter
def insertLetter(letter, pos):
    board[pos] = letter

# Print board in tic-tac-toe format
# Set the list from 1-9 on the board to be modified throughout the program
def printBoard():
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

# Checks if the space is empy - Returns boolean
def isFreeSpace(pos):
    return  board[pos] == ' '
   
# Checks if the board is full by counting the amount of empty spaces (if applicable) - Returns boolean
def isBoardFull(board):
    count = board.count(' ')
    # If there is an empty space, board is not full
    if count > 1:
        return False
    else:
        return True

    # Take amount of parameter and randomize number < parameter
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def compMove():
    # Check for all possible moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            # Creates new empty list
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    # Will check if corners are open
    cornersOpen = []
    # Check the corners and add to list if they are open
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # If there are corners open, select random edge
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # If the middle is open, move there
    if 5 in possibleMoves:
        move = 5
        return move
    
    # Create list for open edges
    edgesOpen = []
    # Check the middle edges and add to list if they are open
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    # If there are edges open, select random corner        
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

     

def playerMove():
    run = True
    # As long as player hasn't found a open space
    while run:
        # Get player input
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if (move > 0) and (move < 10):
                # Is the space free?
                if isFreeSpace(move):
                    # Player found open space
                    run = False
                    # Put 'X' on the board
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Checks if letter (X or O) have valid patterns
def isWinner(board, letter):
    # Possible winning condiitons

    return ((board[1] == letter and board[2] == letter and board[3] == letter) or   # Horizontal top
    (board[4] == letter and board[5] == letter and board[6] == letter) or           # Horizontal Middle
    (board[7] == letter and board[8] == letter and board[9] == letter) or           # Horizontal Bottom
    (board[1] == letter and board[4] == letter and board[7] == letter) or           # Vertical Left
    (board[2] == letter and board[5] == letter and board[8] == letter) or           # Vertical Middle
    (board[3] == letter and board[6] == letter and board[9] == letter) or           # Vertical Right
    (board[1] == letter and board[5] == letter and board[9] == letter) or           # Diagonal Right to Left
    (board[3] == letter and board[5] == letter and board[7] == letter))             # Diagonal Left to Right
    pass

def main():
    # Main Loop

    print("Welcome to Tic Tac Toe! Type in a number between 1-9 to place an 'X' on the board \n")
    printBoard()

    # While board isn't full
    while not(isBoardFull(board)):
       # Is Computer not the winner?
       if not(isWinner(board, 'O')):
           # Player's turn
           playerMove()
           printBoard()
       # Computer Wins
       else:            
           print('Sorry, O\'s won this time!')
           break

       # Is Player not the winner?
       if not(isWinner(board, 'X')):
           # Computer's turn
           move = compMove()
           # If there are no more moves
           if move == 0:
               print('Tie Game!')
           else:
               # Computer's turn
               insertLetter('O', move)
               print('Computer placed an \'O\' in position', move , ':')
               printBoard( )
       else:
            # Player wins
            print('X\'s won this time! Good Job!')
            break
    # If the board is full
    if isBoardFull(board):
        print('Tie Game!')

# Will run till answer isn't 'y' or 'yes'
while True:
    answer = input("Would you like to play again? y/n")
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        board = [' ' for x in range(10)]
        print("-------------------------")
        # Play game
        main()
    else:
        break
