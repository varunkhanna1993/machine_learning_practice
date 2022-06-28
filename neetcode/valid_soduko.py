import collections

def valid_soduku(board):
    ## first we need three hash maps to check for validation
    # row
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)


    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            if (board[i][j] in rows[j] or 
            board[i][j] in cols[i] or 
            board[i][j] in squares[(i//3,j//3)]
            ):
                return False
            rows[j].add(board[i][j])
            cols[i].add(board[i][j])
            squares[(i//3, j//3)].add(board[i][j])

    return True
            



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# print(len(board))
valid_soduku(board)