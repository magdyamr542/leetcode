def threeSum(nums):
    result  = [] # contains the list of arrays
    nums.sort()
    for i in range(len(nums) - 1):
        curr_left = nums[i]
        left = i + 1
        right = len(nums) - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        while left < right: 
            curr_sum = curr_left + nums[left] + nums[right]
            # we need to make the curr_sum bigger to reach the zero by incrementing right counter
            if curr_sum < 0:
                left += 1
            elif curr_sum > 0:
                right -= 1
            else:
                result.append([ curr_left , nums[left] , nums[right] ])
                left += 1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left +=1 
                
            
    return result
        


# https://leetcode.com/problems/3sum/
def main():
    nums = [-2,-1,0,1,1,2]
    print(threeSum(nums))

if __name__ == "__main__":
    main()
