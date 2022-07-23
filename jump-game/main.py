def canJump(nums):
    if len(nums) == 1:
        return True
    
    curr_steps = nums[0]
    
    index = 0
    while curr_steps > 0 and index < len(nums):
        if index + curr_steps >= len(nums) - 1:
            return True
        index += 1
        curr_steps -= 1
        if index < len(nums) and nums[index] > curr_steps:
            curr_steps = nums[index]
        
        
    return False
    

# https://leetcode.com/problems/3sum/
def main():
    nums = [2,3,1,1,4]
    print(canJump(nums))

if __name__ == "__main__":
    main()
