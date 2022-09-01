def count1Bits(n : int):
    base = 1
    result = 0
    while base <= n:
        if base & n > 0:
            # 1 bit found
            result += 1
        base *= 2
    return result
    

            
                
# https://leetcode.com/problems/number-of-1-bits/
if __name__ == "__main__":
    print(count1Bits(5))


    
