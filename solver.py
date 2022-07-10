def print_board(board):             #  Printing the board



    boardString = ''
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += '| '

            if j + 1 == 9:
                boardString += '\n'

            if j + 1 == 9 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += '- - - - - - - - - - - \n'
    print(boardString)


def find_empty(board):                  #    Finding an empty cell to return its position as a tuple


    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)


def valid(board, pos, num):            # check the validity of a number in a cell

    #check for column

    for i in range(9):
        if board[i][pos[1]] == num and (i, pos[1]) != pos:  # checking that the pos is not same in comparing
            return False

    #check for row

    for j in range(9):
        if board[pos[0]][j] == num and (pos[0], j) != pos:
            return False

    #check for cell

    starting_i = pos[0] - pos[0] % 3
    starting_j = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):
            if board[starting_i + i][starting_j + j] == num and (starting_i + i,
                    starting_j + j) != pos:
                return False
    return True


def solve(board):                              # solve the board using backtrack


    empty = find_empty(board)

    if not empty:
        return True

    for num in range(9):
        if valid(board, empty, num + 1):
            board[empty[0]][empty[1]] = num + 1

            if solve(board):
                return True
            board[empty[0]][empty[1]] = 0
    return False


if __name__ == '__main__':
    board =  [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ]
    solve(board)
    print_board(board)