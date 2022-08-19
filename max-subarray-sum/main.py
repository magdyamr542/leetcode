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
    



# https://leetcode.com/problems/maximum-subarray/
def main():
    print(f"this max sum is " , maxSum([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
    main()
