from typing import List

def findNumberOfLIS(nums: List[int]) -> int:
    # at the begining every number is a subsequence of length 1
    dp = [1 for i in range(len(nums))]
    count = [1 for i in range(len(nums))]

    # the first in dp will always have 1 as value
    for i in range(1 , len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                old = dp[i]
                new = dp[j] + 1
                if new > old:
                    dp[i] = new
                    count[i] = count[j]
                elif new == old:
                    count[i] += count[j]


    maximum = max(dp)

    result = 0
    for i in range(len(dp)):
        if dp[i]  == maximum:
            result += count[i]

    return result

# https://leetcode.com/problems/longest-increasing-subsequence/
def main():
    nums = [1,2,4,3,5,4,7,2]

    print(findNumberOfLIS(nums))

if __name__ == "__main__":
    main()
