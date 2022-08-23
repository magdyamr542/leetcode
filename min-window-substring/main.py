def minWindow(s: str, t: str) -> 'str':
    if not t or not s:
        return "" 
    
    # a map of the chars in t with their freqs
    tmap = {}
    for char in t:
        if tmap.get(char , None):
            tmap[char] += 1
        else:
            tmap[char] = 1

    # a map of the currwindow
    currwindow = {}
    
    target = len(tmap) # the target is the number of chars in t. once the window char freqs reaches the target. the window is valid
    
    currwindowCounter = 0 # when the currWindowCounter reaches target. we know the currwindow is valid
    
    result = None # the substring result
    
    # a sliding window where the right pointer gets incremented in order to reach a valid window. when that happens the left pointer gets incremented in order to decrease the window
    left = 0
    right = 0
    while right < len(s):
        currchar = s[right]
        currwindow[currchar] = currwindow.get(currchar , 0) + 1 # save the freq of the curr char in the curr window
        
        if currchar in tmap and currwindow[currchar] == tmap[currchar]:
            currwindowCounter += 1
            
            
        print(currwindowCounter , currchar , currwindow , currwindow )
        while left <= right and currwindowCounter == target:
            # save the best answer
            if  not result or right - left + 1 < len(result) :
                result  = s[left : right + 1]
                
            currLeftChar = s[left]
            currwindow[currLeftChar] -= 1
            
            # decrement the left pointer 
            if currLeftChar in tmap and currwindow[currLeftChar] < tmap[currLeftChar]:
                currwindowCounter -= 1
                
            left += 1
            
        right += 1
        
        
    return "" if not result else result 

# https://leetcode.com/problems/minimum-window-substring/solution/
if __name__ == "__main__":
    print(minWindow("aa" , "aa"))
