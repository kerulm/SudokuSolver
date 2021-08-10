board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def printBoard(board) :
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 : 
                print(" | ", end ="")
            
            if j == 8: 
                print(board[i][j])
            else: 
                print(str(board[i][j]) + " ", end = "")
def emptySpace(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None
def checkValid(board, number, pos):
    #check row
     
    for i in range(len(board[0])):
        if board[pos[0][i]] == number and pos[1] != i: 
            return False
    #check col

    for i in range(len(board[0])):
        if board[pos[i][1]] == number and pos[0] != i: 
            return False

    #check cube you're in

    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == number and (i, j) != pos: 
                return False
    return True

def solve(board): 
    find = emptySpace(board)
    if not find: 
        return True
    else: 
        row, col = find
    for i in range(1, 10):
        if checkValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

printBoard(board)
solve(board)
printBoard(board)
        
            



