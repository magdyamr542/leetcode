def get_permutations(nums):
    result = [] # will hold all permutations
    curr_perm = []
    def dfs(result , choices , curr_perm , count):
        if len(curr_perm) == count:
            result.append(curr_perm.copy())
            return

        for index  , num in enumerate(choices):
            new_choices = choices[:index] + choices[index + 1:]
            dfs(result , new_choices , curr_perm + [num] , count)

    dfs(result , nums , curr_perm , len(nums))
    return result





def main():
    nums = [1,2 , 3]
    print("nums" , nums)
    perms = get_permutations(nums)
    print(f"{len(perms)} permutations")
    print(perms)

if __name__ == "__main__":
    main()
