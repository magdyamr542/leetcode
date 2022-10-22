from typing import List 


def deleteAndEarnBacktracking(nums : List[int]) -> int:
    if len(nums) == 1:
        return nums[0] 

    nums.sort()
    # (num,its freq)
    numCount : List[List[int]] = [[nums[0] , 1]]
    for num in nums[1:]:
        if numCount[-1][0] == num:
            numCount[-1][1] += 1
        else:
            numCount.append([num,1])

    def backtrack(currRes : int , currCombs : List[List[int]])->int:
        if len(currCombs) == 0:
            return currRes 

        if len(currCombs) == 1:
            return currRes + currCombs[0][0] * currCombs[0][1]

        if currCombs[0][0] + 1 == currCombs[1][0]:
            # either take the 0 combination but leave its next one 
            # or leave it and take the next one
            return max(
                backtrack(currRes + currCombs[0][0] * currCombs[0][1] , currCombs[2:]),
                backtrack(currRes, currCombs[1:]),
            )
        else:
            # take the curr combination because there is no conflict
            return backtrack(currRes + currCombs[0][0] * currCombs[0][1] , currCombs[1:])

        # either take the first combination or leave it

    return backtrack(0,numCount)
            

def deleteAndEarnDp(nums : List[int]) -> int:
    if len(nums) == 1:
        return nums[0] 

    nums.sort()
    # (num,its total summed val)
    numCount : List[List[int]] = [[nums[0] , nums[0]]]
    for num in nums[1:]:
        if numCount[-1][0] == num:
            numCount[-1][1] += num
        else:
            numCount.append([num,num])

    dp =  [[0,0] for _ in numCount]
    dp[-1] = numCount[-1]
    for i in range(len(dp)-2 , -1 , -1):
        num ,total  = numCount[i]
        nextNum, nextTotal = dp[i+1]
        if num + 1 != nextNum:
            dp[i] = [num,total + nextTotal]
        else:
            nextNextTotal = dp[i+2][1] if i+2 < len(dp) else 0
            if nextTotal > total + nextNextTotal:
                dp[i] = [nextNum , nextTotal]
            else:
                dp[i] = [num , total + nextNextTotal]


    return dp[0][1]


                
# https://leetcode.com/problems/delete-and-earn/
if __name__ == "__main__":
    nums = [7,7,6,6,3,3,5]
    print(deleteAndEarnDp(nums))


    
