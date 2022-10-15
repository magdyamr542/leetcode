def countSubstrings(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    
    # maps a substring length to a list of the indexes of substrings that are of that length
    # {2 : [(0,1)]} means there is a substring starting at 0 and ending at 1 
    m = {}
    for i in range(1 , len(s) + 1):
        m[i] = []
    
    
    m[1] = [(i,i) for i in range(len(s))] 
    if len(s) >= 2:
        m[2] = [(i,i+1) for i in range(len(s)) if i+1 < len(s) and s[i] == s[i+1]] 
        
    for currLen in range(3 , len(s) + 1):
        # find palyndromic substrings of currLen using info that we have about
        # palyndromic substrings of lengths 1,2,...,currLen-1
        candidates = m[currLen - 2]
        for candidate in candidates:
            start , end = candidate
            # we know the curr candidate is a playndromic substring of length currLen - 2
            # can this candidate be expanded with 2 chars one to the left and one to the right
            # to create a palyndromic substring of len currLen?
            if start - 1 > -1 and end + 1 < len(s) and s[start-1] == s[end+1]:
                m[currLen].append((start-1,end+1))
                    
    result = 0
    for arr in m.values():
        result += len(arr)
    return result
    
    

            
                
# https://leetcode.com/problems/palindromic-substrings/
if __name__ == "__main__":
    print(countSubstrings("abcba"))


    
