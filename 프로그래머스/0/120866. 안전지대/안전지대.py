def solution(board):
    cnt = 0
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for row_move in [-1, 0, 1]:
                    for col_move in [-1, 0, 1]:
                        new_i = i + row_move
                        new_j = j + col_move
                        if 0 <= new_i < n and 0 <= new_j < n:
                            if board[new_i][new_j] == 0:
                                board[new_i][new_j] = 2
             
            
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
    
    return cnt