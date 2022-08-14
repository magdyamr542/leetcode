def get_parentheses(n):
    result = [] # will hold all parentheses
    def dfs(result , num_left , num_right, curr_str):
        if num_left == 0 and num_right == 0:
            # we used all possible parentheses
            result.append(curr_str)
            return

        if num_left > 0:
            dfs(result , num_left - 1 , num_right , curr_str + '(')
        if num_right  > num_left:
            dfs(result , num_left  , num_right - 1 , curr_str + ')')


    dfs(result , n , n , '')
    return result




# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# https://leetcode.com/problems/generate-parentheses/
def main():
    n = 3
    print("n:" , n)
    result = get_parentheses(n)
    print(f"{len(result)} parentheses")
    print(result)

if __name__ == "__main__":
    main()
