def subsets(nums):
    nums.sort()
    result = []
    def dfs(curr_subset , index):
        if index >= len(nums):
            result.append(curr_subset)
            return
        # taking the first choice
        dfs(curr_subset + [nums[index]] , index + 1)
        # not taking the first choice
        while index + 1 < len(nums) and nums[index + 1] == nums[index]:
            index +=1 
        dfs(curr_subset , index + 1)
    dfs([] , 0)
    return result

# https://leetcode.com/problems/subsets-ii/submissions/
if __name__ == "__main__":
    print(subsets([4,4,4,1,4]))
