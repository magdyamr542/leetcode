from typing import List 

def perms(nums : List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def perms(curr_nums , curr_perm):
        # base case
        if len(curr_perm) == len(nums):
            result.append(curr_perm)
            return
            
        for i in range(len(curr_nums)):
            if i > 0 and curr_nums[i] == curr_nums[i-1]:
                continue
            rest_nums = curr_nums[:i] + curr_nums[i+1:]
            perms(rest_nums , curr_perm + [curr_nums[i]])

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        rest_nums = nums[:i] + nums[i+1:]
        perms(rest_nums , [nums[i]])

    return result
        
                
                
# https://leetcode.com/problems/permutations-ii/submissions/
if __name__ == "__main__":
    print(perms([1,2,1]))


    
