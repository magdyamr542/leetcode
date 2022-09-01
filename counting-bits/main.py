def countBits(num : int):
    # if the number is even the most right bit is always 0. e.g 6=110
    # if the number is odd the most right bit is always 1. e.g 5=101
    # shifting to the right means that we get rid of the most right bit. in case of even numbers this is not important since the bit is 0
    # that is way the num of bits for an even number= num of bits for event number / 2
    # for an odd num. we add 1 (the most right bit) + num of bits for num / 2
    if num == 0:
        return [0]
    if num == 1:
        return [0 , 1]
    result = [0 ,1 ]
    for curr in range(2,  num + 1):
        # if even
        if curr % 2 == 0:
            result.append(result[curr // 2])
        else:
            result.append(1 + result[curr // 2])
    return result


            
                
# https://leetcode.com/problems/counting-bits/
if __name__ == "__main__":
    print(countBits(5))


    
