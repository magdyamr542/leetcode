# dynamic programming approach
def maxSum(nums):
    if len(nums) == 1:
        return nums[0]
    
    result = nums[0]
    currentMaxSum = nums[0]
    for i in range(1 , len(nums)):
        num = nums[i]
        currentMaxSum = max(num , currentMaxSum + num)
        result = max(result , currentMaxSum)
    return result
    

# divide and conqur approach
def maxSumDivideAndConqur(nums):
    def maxCross(left , mid , right):
        # get the max sum of the subarray that goes from the middle to the left
        leftMax = 0 
        leftSum = 0 
        for i in range(mid , left - 1 , -1):
            leftSum += nums[i]
            leftMax = max(leftMax , leftSum)

        rightMax = 0 
        rightSum = 0 
        for i in range(mid + 1 , right + 1):
            rightSum += nums[i]
            rightMax = max(rightSum , rightMax)

        return leftMax + rightMax

    def maxSumUtil(left , right):
        # base case
        if left == right:
            return nums[left]
        # divide and conqur
        mid = (right + left) // 2
        maxLeft = maxSumUtil(left , mid)
        maxRight = maxSumUtil(mid + 1 , right)
        crossMax = maxCross(left , mid  , right) # the max sum of the subarray that crosses the middle 
        return max(maxLeft , maxRight , crossMax)

    return maxSumUtil(0 , len(nums) - 1)
    



# https://leetcode.com/problems/maximum-subarray/
def main():
    print(f"this max sum is " , maxSum([-2,1,-3,4,-1,2,1,-5,4]))
    print(f"this max sum divide and conqor is " , maxSumDivideAndConqur([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
    main()
