def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False 
    
    count1 = [0] * 26 # count of char frequencies in s1
    count2 = [0] * 26 # count of char frequencies in s2
    count = 0 # the number of similar frequencies between s1 and the window in s2
    
    for i in range(len(s1)):
        char1 = s1[i]
        count1[ord(char1) - ord('a')] += 1
        
        char2 = s2[i]
        count2[ord(char2) - ord('a')] += 1
        
    for i in range(26):
        if count1[i] == count2[i]:
            count += 1
    
    left = 0
    for right in range(len(s1), len(s2)):
        if count == 26:
            return True # the windows are similar 
        
        char2 = s2[right]
        if count2[ord(char2) - ord('a')] == count1[ord(char2) - ord('a')]:
            # be adding the current right char to the window.
            # we make the frequencies different. so decrement count
            count -= 1
        elif count2[ord(char2) - ord('a')] + 1 == count1[ord(char2) - ord('a')]:
            # be adding the current right char to the window.
            # we make the frequencies equal. so increment count
            count += 1
            
        count2[ord(char2) - ord('a')] += 1 # add the right char to the window
            
        charLeft = s2[left]
        if count2[ord(charLeft) - ord('a')] == count1[ord(charLeft) - ord('a')]:
            # be removing the left char from the window.
            # we make the frequencies different. so decrement count
            count -= 1
        elif count2[ord(charLeft) - ord('a')] - 1 == count1[ord(charLeft) - ord('a')]:
            # be removing the left char from the window.
            # we make the frequencies equal. so increment count
            count += 1
            
        count2[ord(charLeft) - ord('a')] -= 1 # rm the left char from the window
        
        left += 1
        
    return count == 26 # return that both windows have the same char frequencies
        
        
    
# https://leetcode.com/problems/permutation-in-string/
if __name__ == "__main__":
    print(checkInclusion("ab" , "dbeeabdf"))


    
