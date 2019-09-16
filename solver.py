from collections import Counter

def sanity(board):
    if len(board) != 9:
        return False
    for row in board:
        if len(row) != 9:
            return False
        for item in row:
            if item not in range(0, 10):
                return False
    else:
        return True

def row(board, index):
    return board[index]

def column(board, index):
    result = []
    for i in range(0, 9):
        result.append(board[i][index])
    return result

def fetcher(board ,down, right):
    return board[down][right]

def square(board, index):
    result = []

    if index in [0, 1, 2]:
        downs = [0, 1, 2]
    if index in [3, 4, 5]:
        downs = [3, 4, 5]
    if index in [6, 7, 8]:
        downs = [6, 7, 8]
    if index in [0, 3, 6]:
        rights = [0, 1, 2]
    if index in [1, 4, 7]:
        rights = [3, 4, 5]
    if index in [2, 5, 8]:
        rights = [6, 7, 8]

    for down in downs:
        for right in rights:
            result.append(fetcher(board, down, right))

    return result

def check_sudoku(board):
    if not sanity(board):
        return None

    for rownum in range(0, 9):
        counted = Counter(row(board, rownum))
        for gliph in counted:
            if gliph != 0 and counted[gliph] != 1:
                return False
    for columnnum in range(0, 9):
        counted = Counter(column(board, columnnum))
        for gliph in counted:
            if gliph != 0 and counted[gliph] != 1:
                return False
    for squarenum in range(0, 9):
        counted = Counter(square(board, squarenum))
        for gliph in counted:
            if gliph != 0 and counted[gliph] != 1:
                return False

    return True
