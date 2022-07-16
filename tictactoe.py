def print_game_board():
    print(f'''
---------
| {board[0]} {board[1]} {board[2]} |
| {board[3]} {board[4]} {board[5]} |
| {board[6]} {board[7]} {board[8]} |
---------
    ''')


def wins():
    for x in check:
        if x == ['X', 'X', 'X']:
            return 'X wins'
    for x in check:
        if x == ['O', 'O', 'O']:
            return 'O wins'
    for i in range(3):
        break


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
count_motion = 0
print('Привет, Данил, давай поиграем!!!')
while True:
    print_game_board()
    row, column = input().split()
    try:
        row, column = int(row), int(column)
        index = (((int(row) - 1) * 3) + (int(column) + 2)) - 3
    except ValueError:
        print('You should enter numbers!')
    else:
        if (row or column) > 3:
            print('Coordinates should be from 1 to 3!')
        elif board[index] not in ("_", " "):
            print('This cell is occupied! Choose another one!')
        else:
            count_motion += 1
            if count_motion % 2 == 1:
                board[index] = 'X'
            elif count_motion % 2 == 0:
                board[index] = 'O'
            rows = [[board[n] for n in range(i, i + 3)] for i in range(0, len(board), 3)]
            columns = [[board[n] for n in range(i, len(board), 3)] for i in range(3)]
            diagonals = [board[::4]] + [board[2:7:2]]
            check = rows + columns + diagonals
            if wins() in ('X wins', 'O wins'):
                print_game_board()
                print(wins())
                break
            elif count_motion == 9:
                print_game_board()
                print('Draw')
                break
