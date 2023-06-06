import chess.pgn
import matplotlib.pyplot as plt

locs = [chess.A1, chess.A2, chess.A3, chess.A4, chess.A5, chess.A6, chess.A7, chess.A8,
     chess.B1, chess.B2, chess.B3, chess.B4, chess.B5, chess.B6, chess.B7, chess.B8,
     chess.C1, chess.C2, chess.C3, chess.C4, chess.C5, chess.C6, chess.C7, chess.C8,
     chess.D1, chess.D2, chess.D3, chess.D4, chess.D5, chess.D6, chess.D7, chess.D8,
     chess.E1, chess.E2, chess.E3, chess.E4, chess.E5, chess.E6, chess.E7, chess.E8,
     chess.F1, chess.F2, chess.F3, chess.F4, chess.F5, chess.F6, chess.F7, chess.F8,
     chess.G1, chess.G2, chess.G3, chess.G4, chess.G5, chess.G6, chess.G7, chess.G8,
     chess.H1, chess.H2, chess.H3, chess.H4, chess.H5, chess.H6, chess.H7, chess.H8]

loc_map = {chess.A1: (7, 0), chess.B1: (7, 1), chess.C1: (7, 2), chess.D1: (7, 3), chess.E1: (7, 4), chess.F1: (7, 5), chess.G1: (7, 6), chess.H1: (7, 7),
                chess.A2: (6, 0), chess.B2: (6, 1), chess.C2: (6, 2), chess.D2: (6, 3), chess.E2: (6, 4), chess.F2: (6, 5), chess.G2: (6, 6), chess.H2: (6, 7),
                chess.A3: (5, 0), chess.B3: (5, 1), chess.C3: (5, 2), chess.D3: (5, 3), chess.E3: (5, 4), chess.F3: (5, 5), chess.G3: (5, 6), chess.H3: (5, 7),
                chess.A4: (4, 0), chess.B4: (4, 1), chess.C4: (4, 2), chess.D4: (4, 3), chess.E4: (4, 4), chess.F4: (4, 5), chess.G4: (4, 6), chess.H4: (4, 7),
                chess.A5: (3, 0), chess.B5: (3, 1), chess.C5: (3, 2), chess.D5: (3, 3), chess.E5: (3, 4), chess.F5: (3, 5), chess.G5: (3, 6), chess.H5: (3, 7),
                chess.A6: (2, 0), chess.B6: (2, 1), chess.C6: (2, 2), chess.D6: (2, 3), chess.E6: (2, 4), chess.F6: (2, 5), chess.G6: (2, 6), chess.H6: (2, 7),
                chess.A7: (1, 0), chess.B7: (1, 1), chess.C7: (1, 2), chess.D7: (1, 3), chess.E7: (1, 4), chess.F7: (1, 5), chess.G7: (1, 6), chess.H7: (1, 7),
                chess.A8: (0, 0), chess.B8: (0, 1), chess.C8: (0, 2), chess.D8: (0, 3), chess.E8: (0, 4), chess.F8: (0, 5), chess.G8: (0, 6), chess.H8: (0, 7)
                }
loc_map_2 = {"a1": (7, 0), "b1": (7, 1), "c1": (7, 2), "d1": (7, 3), "e1": (7, 4), "f1": (7, 5), "g1": (7, 6), "h1": (7, 7),
                "a2": (6, 0), "b2": (6, 1), "c2": (6, 2), "d2": (6, 3), "e2": (6, 4), "f2": (6, 5), "g2": (6, 6), "h2": (6, 7),
                "a3": (5, 0), "b3": (5, 1), "c3": (5, 2), "d3": (5, 3), "e3": (5, 4), "f3": (5, 5), "g3": (5, 6), "h3": (5, 7),
                "a4": (4, 0), "b4": (4, 1), "c4": (4, 2), "d4": (4, 3), "e4": (4, 4), "f4": (4, 5), "g4": (4, 6), "h4": (4, 7),
                "a5": (3, 0), "b5": (3, 1), "c5": (3, 2), "d5": (3, 3), "e5": (3, 4), "f5": (3, 5), "g5": (3, 6), "h5": (3, 7),
                "a6": (2, 0), "b6": (2, 1), "c6": (2, 2), "d6": (2, 3), "e6": (2, 4), "f6": (2, 5), "g6": (2, 6), "h6": (2, 7),
                "a7": (1, 0), "b7": (1, 1), "c7": (1, 2), "d7": (1, 3), "e7": (1, 4), "f7": (1, 5), "g7": (1, 6), "h7": (1, 7),
                "a8": (0, 0), "b8": (0, 1), "c8": (0, 2), "d8": (0, 3), "e8": (0, 4), "f8": (0, 5), "g8": (0, 6), "h8": (0, 7)
                }

def increase_board(big_board, index):
    if index[0] >=0 and index[0] <= 7 and index[1] >= 0 and index[1] <= 7:
        big_board[index[0]][index[1]] += 1
    return big_board

def analyze_black_pawn(big_board, loc):
    index = loc_map[loc]
    big_board = increase_board(big_board, (index[0] + 1, index[1] - 1))
    big_board = increase_board(big_board, (index[0] + 1, index[1] + 1))
    return big_board

def analyze_white_pawn(big_board, loc):
    index = loc_map[loc]
    big_board = increase_board(big_board, (index[0] - 1, index[1] - 1))
    big_board = increase_board(big_board, (index[0] - 1, index[1] + 1))
    return big_board

def analyze_rook(big_board, loc):
    index = loc_map[loc]
    for i in range(8):
        big_board = increase_board(big_board, (index[0], i))
        big_board = increase_board(big_board, (i, index[1]))
    return big_board

def analyze_knight(big_board, loc):
    index = loc_map[loc]
    big_board = increase_board(big_board, (index[0] + 2, index[1] + 1))
    big_board = increase_board(big_board, (index[0] + 2, index[1] - 1))
    big_board = increase_board(big_board, (index[0] - 2, index[1] + 1))
    big_board = increase_board(big_board, (index[0] - 2, index[1] - 1))
    big_board = increase_board(big_board, (index[0] + 1, index[1] + 2))
    big_board = increase_board(big_board, (index[0] + 1, index[1] - 2))
    big_board = increase_board(big_board, (index[0] - 1, index[1] + 2))
    big_board = increase_board(big_board, (index[0] - 1, index[1] - 2))
    return big_board

def analyze_bishop(big_board, loc): 
    index = loc_map[loc]
    for i in range(8):
        big_board = increase_board(big_board, (index[0] + i, index[1] + i))
        big_board = increase_board(big_board, (index[0] - i, index[1] + i))
        big_board = increase_board(big_board, (index[0] + i, index[1] - i))
        big_board = increase_board(big_board, (index[0] - i, index[1] - i))
    return big_board

def analyze_queen(big_board, loc):
    index = loc_map[loc]
    for i in range(8):
        big_board = increase_board(big_board, (index[0], i))
        big_board = increase_board(big_board, (i, index[1]))
        big_board = increase_board(big_board, (index[0] + i, index[1] + i))
        big_board = increase_board(big_board, (index[0] - i, index[1] + i))
        big_board = increase_board(big_board, (index[0] + i, index[1] - i))
        big_board = increase_board(big_board, (index[0] - i, index[1] - i))
    return big_board

def analyze_king(big_board, loc):
    index = loc_map[loc]
    big_board = increase_board(big_board, (index[0] + 1, index[1] + 1))
    big_board = increase_board(big_board, (index[0] + 1, index[1] - 1))
    big_board = increase_board(big_board, (index[0] - 1, index[1] + 1))
    big_board = increase_board(big_board, (index[0] - 1, index[1] - 1))
    big_board = increase_board(big_board, (index[0] + 1, index[1]))
    big_board = increase_board(big_board, (index[0] - 1, index[1]))
    big_board = increase_board(big_board, (index[0], index[1] + 1))
    big_board = increase_board(big_board, (index[0], index[1] - 1))
    return big_board


def analyze_board(big_board, board):
    
    # pieces = {'p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K'}
    for loc in locs:
        piece = board.piece_at(loc)
        if piece is not None:
            p = piece.symbol()
            if p == 'p':
                big_board = analyze_black_pawn(big_board, loc)
            elif p == 'r' or p == 'R':
                big_board = analyze_rook(big_board, loc)
            elif p == 'n' or p == 'N':
                big_board = analyze_knight(big_board, loc)
            elif p == 'b' or p == 'B':
                big_board = analyze_bishop(big_board, loc)
            elif p == 'q' or p == 'Q':
                big_board = analyze_queen(big_board, loc)
            elif p == 'k' or p == 'K':
                big_board = analyze_king(big_board, loc) 
            elif p == 'P':
                big_board = analyze_white_pawn(big_board, loc)
    return big_board
            

def update_move_board(move_board, row, col):
    if row >=0 and row <= 7 and col >= 0 and col <= 7:
        move_board[row][col] += 1
    return move_board

def analyze_move(move_board, mover):
    col_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    #convert move to string
    move = str(mover)
    print(move)
    start_row, start_col = loc_map_2[move[0:2]]
    print(start_col, start_row)
    end_row, end_col = loc_map_2[move[2:4]]
    
    # start_col = int(col_to_num[move[0]])
    # start_row = int(move[1]) - 1
    # end_col = int(col_to_num[move[2]])
    # end_row = int(move[3]) - 1
    if start_col == end_col:
        # vertical move
        for i in range(min(start_row, end_row), max(start_row, end_row)+1):
            move_board = update_move_board(move_board, i, start_col)
    elif start_row == end_row:
        # horizontal move
        for i in range(min(start_col, end_col), max(start_col, end_col)+1):
            move_board = update_move_board(move_board, start_row, i)
    elif abs(start_col - end_col) == abs(start_row - end_row):
        # diagonal move
        for i in range(abs(start_col - end_col)+1):
            move_board = update_move_board(move_board, min(start_row, end_row) + i, min(start_col, end_col) + i)
    else:
        # knight move
        # default to do the 1 first and then the two
        move_board = update_move_board(move_board, start_row, start_col)
        if abs(start_row - end_row) == 1:
            # 1 row shift
            move_board = update_move_board(move_board, end_row, start_col)
            if end_col > start_col:
                move_board = update_move_board(move_board, end_row, start_col + 1)
                move_board = update_move_board(move_board, end_row, start_col + 2)
            else:
                move_board = update_move_board(move_board, end_row, start_col - 1)
                move_board = update_move_board(move_board, end_row, start_col - 2)
        else:
            # 1 col shift
            move_board = update_move_board(move_board, start_row, end_col)
            if end_row > start_row:
                move_board = update_move_board(move_board, start_row + 1, end_col)
                move_board = update_move_board(move_board, start_row + 2, end_col)
            else:
                move_board = update_move_board(move_board, start_row - 1, end_col)
                move_board = update_move_board(move_board, start_row - 2, end_col)
    return move_board


def simulate_game(pgn_file, big_board, move_board):
    with open(pgn_file) as f:
        game = chess.pgn.read_game(f)

    board = game.board()

    print("Simulating chess game...\n")

    for move in game.mainline_moves():
        board.push(move)
        print(f"Move: {move}")
        move_board = analyze_move(move_board, move)
        # print(f"Board:\n{board}\n")
        big_board = analyze_board(big_board, board)
        # print(big_board)
    # print(move_board)
    print("Game over.")
    print("Result: " + game.headers["Result"])


# Example usage:

big_board = [[0 for _ in range(8)] for _ in range(8)]
move_board = [[0 for _ in range(8)] for _ in range(8)]
pgn_file = "gukesh_giri_norway_chess_2023.pgn"
simulate_game(pgn_file, big_board, move_board)
for i in move_board:
    print(i)

# print move_board as a heat map
plt.imshow(move_board, cmap='hot', interpolation='nearest')
plt.show()