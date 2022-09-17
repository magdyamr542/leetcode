

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    
    first = 1
    second = 2
    for i in range(2,n):
        tmp = first
        first = second
        second = second + tmp 
    return  second
        
    

# https://leetcode.com/problems/climbing-stairs/
def main():
    print(climbStairs(4))

if __name__ == "__main__":
    main()
