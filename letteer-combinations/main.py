def get_letter_combinations(digits):
    result = [] # will hold the letter combinations
    lettter_to_char = {}
    lettter_to_char["2"] =list("abc")
    lettter_to_char["3"] =list("def")
    lettter_to_char["4"] =list("ghi")
    lettter_to_char["5"] =list("jkl")
    lettter_to_char["6"] =list("mno")
    lettter_to_char["7"] =list("pqrs")
    lettter_to_char["8"] =list("tuv")
    lettter_to_char["9"] =list("wxyz")
    digits.center
    if len(digits) == 1:
        return lettter_to_char[digits[0]]

    def dfs(remaining_digits , curr_combination , result):
        # base case
        if len(remaining_digits) == 0:
            result.append(curr_combination)
            return
        # generate the combinations
        curr_digit = remaining_digits[0]
        for char in lettter_to_char[curr_digit]:
            dfs(remaining_digits[1:] ,curr_combination + char , result )

    dfs(list(digits) , "" , result)

    return result



# problem definition: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def main():
    digits = "23"
    combinations = get_letter_combinations(digits)
    print("combinations:")
    print(combinations)

if __name__ == "__main__":
    main()
