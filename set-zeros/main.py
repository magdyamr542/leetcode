from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    cols = len(matrix[0])
    rows = len(matrix)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "x":
                continue
            if matrix[row][col] == 0:
                for colIndex in range(0 ,cols):
                    if matrix[row][colIndex] != 0:
                        matrix[row][colIndex] = "x"
    
                for rowIndex in range(0 ,rows):
                    if matrix[rowIndex][col] != 0:
                        matrix[rowIndex][col] = "x"
                        
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "x":
                matrix[row][col] = 0

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(matrix)
    setZeroes(matrix)
    print(matrix)
