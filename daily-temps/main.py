from typing import List


def dailyTemperatures(temps: List[int]) -> List[int]:
    # use an increasing stack to store temps and their indexes
    # one you get a temp that is bigger than the top of the stack. pop it and update its result value.
    stack = [] # stack of tuples (temp , index)
    answer = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[stack[-1]] < temps[i]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
    return answer
            
        
    


# https://leetcode.com/problems/daily-temperatures/
def main():
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))

if __name__ == "__main__":
    main()
