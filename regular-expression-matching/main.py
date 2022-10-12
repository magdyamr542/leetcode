def isMatch(s: str, p: str) -> bool:
    # base cases
    def helper(s,p):
        # everything is processed
        if len(s) == 0 and len(p) == 0:
            return True
        
        if len(p) == 0:
            return False # patter is processed but input not yet
        
        if len(s) == 0:
            # the pattern is not empty yet but the input is
            # the pattern should be of the form '[char]*[char]*' and so on
            oddChars = set()
            for i in range(len(p)):
                if i % 2 == 1:
                    oddChars.add(p[i])
            return len(oddChars) == 1 and "*" in oddChars and len(p) % 2 == 0 # odd chars are astrik only
                    
       
        # here bot s and p have len > 0
        shouldExpand = len(p) > 1 and p[1] == "*"
        if shouldExpand:
            # the curr char can be expanded because it's followed by astrik.
            # here we have 2 possibilities. either to not use it or use it more than once
            notExpanding = helper(s , p[2:])
            if notExpanding:
                return True
            expanding = helper(s , p[0] + p) 
            return expanding
        else:
            # the curr char cannot be expanded. match literally or with a .
            if p[0] == ".":
                return helper(s[1:] , p[1:])
            else:
                return s[0] == p[0] and helper(s[1:] , p[1:])
        
    return helper(s,p)    
    

            
                
# https://leetcode.com/problems/regular-expression-matching/
if __name__ == "__main__":
    print(isMatch("ab" , ".*"))


    
