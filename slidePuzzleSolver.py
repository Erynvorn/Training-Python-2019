def is_solved(board):
    size = len(board[0])
    print(size)
    for i in range(size):
        for j in range(size):
            print(board[i][j])
            if board[i][j] != i*size+j:
                return False
    return True
