def get_combs(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [ nums ]
    result = [] # this list hold all permutations
    for i in range(len(nums)):
        current_perm = [nums[i]] # use current num for this
        rem_list = nums[:i] + nums[i+1:] # rm current num from the list
        for p in get_combs(rem_list):
            result.append(current_perm + p)
    return result

def main():
    combs = get_combs([1 , 2,3])
    print("combinations")
    print(combs)

if __name__ == "__main__":
    main()
