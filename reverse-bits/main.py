def reverseBits(n : int):
    print("input=" , "{0:b}".format(n))
    result = 0
    count = 0
    while n != 0:
        count += 1
        if n % 2 == 0:
            # most left bit is zero
            result *= 2
        else:
            # most left bit is one
            result = result * 2 + 1
        n = n >> 1 
        
    while count < 32:
        count += 1
        result *= 2

    print("count=" , count)
    print("output=" , "{0:b}".format(result))
    print("output=" , result)

    return result


            
                
# https://leetcode.com/problems/reverse-bits/
if __name__ == "__main__":
    print(reverseBits(43261596))


    
