from typing import List

def can_build_word(board: List[List[str]], word: str) -> bool:
    rows = len(board) 
    cols = len(board[0]) 
    # track visited chars
    visited = [[False for col in range(cols)] for row in range(rows)]
    # main backtracking function
    def dfs(row , col , board , visited , word) -> bool:
        # return true if the word can be constructed and we begin by char at board[row][col]
        
        # base case: we constructed the word
        if len(word) == 0:
            return True
        
        # check out of bounds
        if row >= rows or row < 0 or col >= cols or col < 0:
            return False
        
        # check if we visited the char before
        if visited[row][col]:
            return False
        
        # check if we can use this char to construct the word
        if board[row][col] != word[0]:
            return False
        
        # use the char and mark it as visited
        visited[row][col] = True
        
        # check if we can construct the rest of the word by bruteforcing all directions
        rest_of_word = word[1:]
        did_build_word =  dfs(row + 1 , col , board , visited , rest_of_word) or dfs(row - 1 , col , board , visited , rest_of_word) or  dfs(row , col + 1, board , visited , rest_of_word) or  dfs(row , col - 1, board , visited , rest_of_word)
                
        if not did_build_word:
            visited[row][col] = False # unvisit the char
            return False
        
        return True

    for row in range(rows):
        for col in range(cols):
            if dfs(row,col,board , visited , word):
                return True
    return False
                
            
        
        
        
# problem description https://leetcode.com/problems/word-search/submissions/
def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print("Board:")
    for i in board:
        print('\t'.join(map(str, i)))
    print(f"Can build {word}:")
    if can_build_word(board , word):
        print("can build")
    else:
        print("cannot build")

if __name__ == "__main__":
    main()
