def reverseBits(n : int):
    print("input=" , "{0:b}".format(n))
    result = 0
    for _ in range(32):
        if n % 2 == 0:
            # most left bit is zero
            result *= 2
        else:
            # most left bit is one
            result = result * 2 + 1
        n = n >> 1 
        

    print("output=" , "{0:b}".format(result))
    print("output=" , result)

    return result


            
                
# https://leetcode.com/problems/reverse-bits/
if __name__ == "__main__":
    print(reverseBits(4294967293))


    
