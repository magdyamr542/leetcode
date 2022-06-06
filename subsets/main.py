def get_subsets(nums):
    result = [] # will hold all subsets
    curr_subset = []

    def dfs(result , choices , curr_subset):
        if len(choices) == 0:
            result.append(curr_subset)
            return

        index = 0
        curr_choice = choices[index]
        dfs(result , choices[:index] + choices[index + 1:]  , curr_subset + [curr_choice]) # use it
        dfs(result , choices[:index] + choices[index + 1:]  , curr_subset) # or don't use i

    dfs(result , nums , curr_subset)

    return result





def main():
    nums = [1,2 , 3]
    print("nums" , nums)
    subsets = get_subsets(nums)
    print(f"{len(subsets)} subsets")
    print(subsets)

if __name__ == "__main__":
    main()
