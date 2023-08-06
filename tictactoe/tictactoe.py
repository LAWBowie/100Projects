def print_board(board):
    print("\n".join([" ".join(row) for row in board]))

def get_move():
    while True:
        move = input("Enter your move as 'row column': ")
        try:
            row, col = map(int, move.split())
            return row - 1, col - 1
        except:
            print("Invalid move. Try again.")

def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True

def has_won(board, player):
    win_states = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    positions = [i for i, x in enumerate(board) if x == player]
    for win_state in win_states:
        if all(pos in positions for pos in win_state):
            return True
    return False

def play():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    
    while True:
        print_board(board)
        row, col = get_move()
        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        if has_won(board, player):
            print(f"Player {player} has won!")
            break
        player = 'O' if player == 'X' else 'X'

play()
