from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    col_start = 0
    col_end = len(matrix[0]) - 1
    
    row_start = 0
    row_end = len(matrix) - 1
    
    result = []
    goto = "right"
    while col_start <= col_end and row_start <= row_end:
        if goto == "right":
            # append items
            for col in range(col_start , col_end + 1):
                result.append(matrix[row_start][col])
            # modify for next position
            goto = "down"
            row_start += 1
        elif goto == "down":
            for row in range(row_start , row_end + 1):
                result.append(matrix[row][col_end])
            goto = "left"
            col_end -= 1
        elif goto == "left":
            for col in range(col_end , col_start - 1 , -1):
                result.append(matrix[row_end][col])
            goto = "up"
            row_end -= 1
        elif goto == "up":
            for row in range(row_end , row_start - 1 , -1):
                result.append(matrix[row][col_start])
            goto = "right"
            col_start += 1
            
        
    return result

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))
