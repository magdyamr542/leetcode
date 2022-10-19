from typing import List



def maxCoinsBacktracing(nums: List[int]) -> int:
    result = 0
    # for each index we can burst the balloon at this index
    # then we use the rest of the array recursivly
    def backtrack(currChoices : List[int] , currResult : int):
        # base case
        if len(currChoices) == 0:
            return currResult

        best = -1
        for i in range(len(currChoices)):
            currAmount = currChoices[i]
            # tak the curr balloon and burst it
            if i - 1 > -1:
                currAmount *= currChoices[i-1]

            if i + 1 < len(currChoices):
                currAmount *= currChoices[i+1]

            restOfChoices = currChoices[:i] + currChoices[i+1:]
            best = max(best , backtrack(restOfChoices  , currResult + currAmount))

        return best

    result = backtrack(nums , 0)

    return result

    

def maxCoinsCaching(nums: List[int]) -> int:
    result = 0
    cache = {}
    # for each index we can burst the balloon at this index
    # then we use the rest of the array recursivly
    def backtrack(currChoices : List[int] , currResult : int):
        if tuple(currChoices) in cache:
            return currResult + cache[tuple(currChoices)]

        # base case
        if len(currChoices) == 0:
            return currResult

        best = -1
        for i in range(len(currChoices)):
            currAmount = currChoices[i]
            # tak the curr balloon and burst it
            if i - 1 > -1:
                currAmount *= currChoices[i-1]

            if i + 1 < len(currChoices):
                currAmount *= currChoices[i+1]

            restOfChoices = currChoices[:i] + currChoices[i+1:]
            newResult = backtrack(restOfChoices  , currResult + currAmount)
            cache[tuple(restOfChoices)] = newResult - (currResult + currAmount)
            best = max(best , newResult)

        return best

    result = backtrack(nums , 0)

    return result

            
                
# https://leetcode.com/problems/burst-balloons/
if __name__ == "__main__":
    print(maxCoinsBacktracing([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2,5,5]))


    
