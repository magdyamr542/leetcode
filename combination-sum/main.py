from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    # contains the combinations
    result = []

    # geneate the combinations when we have the currentSum with the currentCombination
    def generateComs(currentSum : int , currentCom : List[int] , startIndex : int ,   result : List[List[int]]):
        # base case
        if currentSum > target:
            # we could not generate the target with the current combination
            return

        if currentSum == target:
            # we generated a combination
            result.append(currentCom)
            return

        # the currentSum is less than the target. generate the combinations
        for i in range(startIndex , len(candidates)):
            num = candidates[i]
            if num < target:
                generateComs(currentSum + num , currentCom + [num] , i, result)

    for i in range(len(candidates)):
        num = candidates[i]
        if num <= target:
            generateComs(num , [num] , i  ,  result)

    return result



def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # contains the combinations
    result = []

    # geneate the combinations when we have the currentSum with the currentCombination
    # it starts searching from the startIndex till the end of the array to avoid duplicates
    def generateComs(currentSum : int , currentCom : List[int] , startIndex : int ,   result : List[List[int]]):
        # base case
        if startIndex >= len(candidates) or currentSum > target:
            # we could not generate the target with the current combination
            return

        if currentSum == target:
            # we generated a combination
            result.append(currentCom)
            return

        # we make 2 decisions. either we consider the current number in the combinations or we don't
        generateComs(currentSum + candidates[startIndex] , currentCom + [candidates[startIndex]] , startIndex , result )
        generateComs(currentSum , currentCom , startIndex + 1 , result )


    generateComs(0 , [] , 0  ,  result)
        
    return result

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates , target))
