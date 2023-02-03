
score = 0
computer = 'X'
player = 'O'

board = [['_'] * 3 for _ in range(3)]

def game_score():
    global score
    if check_win() == computer:
        print("Sorry, but the computer won!")
        score -= 1
    elif check_win() == player:
        print("You won!")
        score += 1
    else:
        print("Draw")



def game_board():
    print("  0 1 2")
    for count, row in enumerate(board):
        print(count, ' '.join(row))
    # draw score
    print(f"Score: {str(score)}")
        
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None

def player_turn():
    while True:
        x, y = input("Enter coordinates: ").split()
        if not (x.isdigit() and y.isdigit()):
            print("You should enter numbers!")
        elif not (0 <= int(x) <= 2 and 0 <= int(y) <= 2):
            print("Coordinates should be from 0 to 2!")
        elif board[int(x)][int(y)] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            board[int(x)][int(y)] = player
            break

def computer_turn():
    from random import randint
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        if board[x][y] == '_':
            board[x][y] = computer
            break

while True:
    game_board()
    player_turn()
    if check_win():
        game_board()
        game_score()
        break
    computer_turn()
    if check_win():
        game_board()
        game_score()
        break
    



