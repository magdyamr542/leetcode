def longestPalindrome(s: str) -> str:
    if len(s) <=1:
        return s
    longest_pal = s[1]
    middle_char_index = 1
    while middle_char_index < len(s):
        curr_pal = s[middle_char_index]
        left = middle_char_index - 1
        right = middle_char_index + 1
        
        while right < len(s) and s[right] == s[middle_char_index]:
            curr_pal += s[right]
            right += 1
            
        while left > -1 and s[left] == s[middle_char_index]:
            curr_pal = s[left] +  curr_pal
            left -= 1
            
            
        while left > -1 and right < len(s) and s[left] == s[right]:
            curr_pal = s[left] + curr_pal + s[right]
            left -= 1
            right += 1
        
        middle_char_index += 1
        if len(curr_pal) > len(longest_pal):
            longest_pal = curr_pal
      
    return longest_pal
        
        
# https://leetcode.com/problems/longest-palindromic-substring/
def main():
    print(longestPalindrome("cammaf"))

if __name__ == "__main__":
    main()
