def isHappy(n):
    # 1,10,100,1000,10000,...
    seen = set()
    while n != 1:
        if n in seen:
            return False
        # set n to the sum of the square of its digits.
        seen.add(n)
        curr = n
        theSum = 0
        while curr != 0:
            theSum += pow((curr % 10),2)
            curr = curr // 10
        n = theSum
            
    return True
    


# https://leetcode.com/problems/happy-number/submissions/
def main():
    print(isHappy(19))

if __name__ == "__main__":
    main()
