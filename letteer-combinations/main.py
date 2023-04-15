from typing import List


def get_letter_combinations(digits : str):
    if not len(digits):
        return []

    result : List[str] = []
    # maps a digit to its corresponding letters
    digitMap = {
        "2" : ["a" , "b" , "c"],
        "3" : ["d" , "e", "f"],
        "4" : ["g" , "h" , "i"],
        "5" : ["j" , "k" , "l"],
        "6" : ["m" , "n" , "o"],
        "7" : ["p" , "q" , "r" , "s"],
        "8" : ["t" , "u" , "v"],
        "9" : ["w" , "x" , "y" , "z"],
    }

    # currIndex points to our location in the digits string
    # currCombination is the string we generated so far
    def dfs(currIndex : int , currCombination: str):
        # base case. done processing the digits string
        if currIndex >= len(digits):
            result.append(currCombination)
            return

        # for all letters we can generate from the current digit, add each of the to the currCombination
        # and then proceed to proces the next digit
        currDigit = digits[currIndex]
        for letter in digitMap[currDigit]:
            dfs(currIndex + 1 , currCombination + letter)

    dfs(0 , "")

    return result




# problem definition: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def main():
    digits = "23"
    combinations = get_letter_combinations(digits)
    print("combinations:")
    print(combinations)

if __name__ == "__main__":
    main()
