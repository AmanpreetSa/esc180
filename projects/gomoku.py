"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""

def is_empty(board):
    board_size = len(board)
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] != " ":
                return False
    return True

def is_full(board):  
    board_size = len(board)
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == " ":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    board_size = len(board)
    y_start = y_end - (length - 1) * d_y
    x_start = x_end - (length - 1) * d_x

    y_before = y_start - d_y
    x_before = x_start - d_x
    y_after = y_end + d_y
    x_after = x_end + d_x

    is_open_before = False
    is_open_after = False

    if 0 <= y_before < board_size and 0 <= x_before < board_size:
        if board[y_before][x_before] == " ":
            is_open_before = True

    if 0 <= y_after < board_size and 0 <= x_after < board_size:
        if board[y_after][x_after] == " ":
            is_open_after = True

    if is_open_before and is_open_after:
        return "OPEN"
    elif is_open_before or is_open_after:
        return "SEMIOPEN"
    else:
        return "CLOSED"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    board_size = len(board)
    open_seq_count = 0
    semi_open_seq_count = 0

    y = y_start
    x = x_start

    while 0 <= y < board_size and 0 <= x < board_size:
        if board[y][x] != col:
            y += d_y
            x += d_x
            continue

        seq_length = 0
        y_seq = y
        x_seq = x

        while 0 <= y_seq < board_size and 0 <= x_seq < board_size and board[y_seq][x_seq] == col:
            seq_length += 1
            y_seq += d_y
            x_seq += d_x

        if seq_length == length:
            y_end = y + (seq_length - 1) * d_y
            x_end = x + (seq_length - 1) * d_x
            y_before = y - d_y
            x_before = x - d_x
            y_after = y_end + d_y
            x_after = x_end + d_x

            is_complete = True

            if 0 <= y_before < board_size and 0 <= x_before < board_size:
                if board[y_before][x_before] == col:
                    is_complete = False

            if 0 <= y_after < board_size and 0 <= x_after < board_size:
                if board[y_after][x_after] == col:
                    is_complete = False

            if is_complete:
                bounded = is_bounded(board, y_end, x_end, length, d_y, d_x)
                if bounded == "OPEN":
                    open_seq_count += 1
                elif bounded == "SEMIOPEN":
                    semi_open_seq_count += 1

        y = y_seq
        x = x_seq

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0

    board_size = len(board)

    # horizontal lines
    for y in range(board_size):
        count_open, count_semi = detect_row(board, col, y, 0, length, 0, 1)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    # vertical lines
    for x in range(board_size):
        count_open, count_semi = detect_row(board, col, 0, x, length, 1, 0)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    # diagonal lines (\)
    for y in range(board_size):
        count_open, count_semi = detect_row(board, col, y, 0, length, 1, 1)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    for x in range(1, board_size):
        count_open, count_semi = detect_row(board, col, 0, x, length, 1, 1)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    # diagonal lines (/)
    for y in range(board_size):
        count_open, count_semi = detect_row(board, col, y, 0, length, -1, 1)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    for x in range(1, board_size):
        count_open, count_semi = detect_row(board, col, board_size - 1, x, length, -1, 1)
        open_seq_count += count_open
        semi_open_seq_count += count_semi

    return open_seq_count, semi_open_seq_count

def search_max(board):
    max_score = -float('inf')
    move_y = None
    move_x = None
    board_size = len(board)
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == ' ':
                board[y][x] = 'b'
                current_score = score(board)
                if current_score > max_score:
                    max_score = current_score
                    move_y = y
                    move_x = x
                board[y][x] = ' '
    return move_y, move_x
        
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    board_size = len(board)
    for col in ['b', 'w']:
        for y in range(board_size):
            for x in range(board_size):
                if board[y][x] == col:
                    for d_y, d_x in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                        if is_seq_complete(board, y, x, d_y, d_x, 5, col):
                            return 'Black won' if col == 'b' else 'White won'
    for row in board:
        if ' ' in row:
            return 'Continue playing'
        if is_full(board)==True:
            return 'Draw'


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
              
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
def sq_on_board(board, y, x):
    n = len(board)
    if not 0<=y < n:
        return False
    if not 0<=x < n:
        return False 
    return True

def is_seq_complete(board, y_start, x_start, d_y, d_x, length, col):
    y = y_start
    x = x_start
    y_prev = y_start - d_y
    x_prev = x_start - d_x
    if sq_on_board(board, y_prev, x_prev):
        if board[y_prev][x_prev] == col:
            return False

    for i in range(length):
        if not sq_on_board(board, y, x) or board[y][x] != col:
            return False
        y += d_y
        x += d_x

    if sq_on_board(board, y, x):
        if board[y][x] == col:
            return False

    return True

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

if __name__ == '__main__':
    play_gomoku(8)
    
