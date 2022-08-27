def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    
    currmap = {}
    left = 0
    right = 0
    result = 0
    while right < len(s) and left < len(s):
        currchar = s[right]
        currmap[currchar] = currmap.get(currchar , 0) + 1
        if currmap[currchar] == 1:
            result = max(right - left + 1 , result)
        while left <= right and currmap[currchar] > 1:
            charleft = s[left]
            # make the window smaller
            currmap[charleft] -= 1
            left += 1
        right += 1
    return result
        
    
    

# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
