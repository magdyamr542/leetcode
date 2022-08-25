def reduce(input: str , k : int) -> str:
    left = 0
    right = 0
    while left < len(input) and right < len(input):
        while right < len(input) and left < len(input) and right - left + 1 < k and input[left] == input[right]:
            right += 1

        if right >= len(input):
            break

        if right - left + 1 == k and input[left] == input[right]:
            # remove 
            input = input[:left] + input[right + 1:]
            left = 0
            right = 0 
        else:
            right += 1
            left += 1

    return input


def reduceWithStack(input: str , k : int) -> str:
    # stack of tuples (x,y). x is the char. y is its consecutive frequency. 
    # once the freq reaches k. remove the entry from the stack
    stack = [] 
    for char in input:
        if len(stack) == 0:
            stack.append([char , 1])
            continue
        stackTop = stack[len(stack) - 1]
        if stackTop[0] == char:
            stackTop[1] += 1
            if stackTop[1] == k:
                # remove it from the stack
                stack.pop()
        else:
            stack.append([char , 1])

    return "".join(list(map(lambda entry : entry[0] , stack)))


        
        

# https://www.geeksforgeeks.org/reduce-the-string-by-removing-k-consecutive-identical-characters/
if __name__ == "__main__":
    print(reduce("qddxxxdxxfffxm" , 3))
    print(reduce("qddxxxdxxfffxm" , 2))
