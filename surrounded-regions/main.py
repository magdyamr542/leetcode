
def surrounded_regions(board):
    # 1. go over cells at the border and start a dfs from there in order to mark other connected
    #   cells as cells that can't be flipped

    # 2. go over all cells and for O cells that are not marked. flip them
    ROWS = len(board)
    COLS = len(board[0])
    can_be_flipped = [[True for __ in range(COLS)]for _ in range(ROWS)] 
    visited = [[False for __ in range(COLS)]for _ in range(ROWS)] 

    # top corner
    for i in range(COLS):
        dfs(board , can_be_flipped , 0 , i  , visited, ROWS , COLS )

    # bottom corner
    for i in range(COLS):
        dfs(board , can_be_flipped , ROWS-1 , i  , visited, ROWS , COLS )

    # left corner
    for i in range(ROWS):
        dfs(board , can_be_flipped , i ,   0  , visited, ROWS , COLS )

    # right corner
    for i in range(ROWS):
        dfs(board , can_be_flipped , i ,   COLS-1  , visited, ROWS , COLS )


    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O" and can_be_flipped[row][col]:
                # flip it
                board[row][col] = "X"



def dfs(board , can_be_flipped , row , col , visited , ROWS , COLS):
    # base case
    if row >= ROWS or row < 0 or col >= COLS or col < 0 or visited[row][col]:
        return

    visited[row][col] = True
    if board[row][col] == "X":
        # not interesting
        return

    can_be_flipped[row][col] = False
    dfs(board , can_be_flipped , row + 1 , col , visited , ROWS , COLS)
    dfs(board , can_be_flipped , row - 1 , col , visited , ROWS , COLS)
    dfs(board , can_be_flipped , row , col +1, visited , ROWS , COLS)
    dfs(board , can_be_flipped , row , col  - 1, visited , ROWS , COLS)

# problem: https://leetcode.com/problems/surrounded-regions/
def main():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print("before")
    print('\n'.join(map(' '.join, board)))
    surrounded_regions(board)
    print("after")
    print('\n'.join(map(' '.join, board)))

if __name__ == "__main__":
    main()
