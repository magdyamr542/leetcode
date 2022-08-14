from typing import List

def evalRPN(tokens: List[str]) -> int:
    # using a stack where we apply the mathematical operation whenever we face an operand at the top of the stack 
    stack = []
    result = 0  
    for token in tokens:
        print(stack)
        if token == "+" or token == "-" or token == "*" or token == "/":
            secondOp = stack.pop()
            firstOp = stack.pop()
            result = 0  
            if token == "+":
                result  = firstOp + secondOp
            elif token == "-":
                result  = firstOp - secondOp
            elif token == "*":
                result  = firstOp * secondOp
            else:
                    result = firstOp / secondOp 
                    
            stack.append(result)
        else:
            stack.append(int(token))
        
    return stack[0]            
            
    

# https://leetcode.com/problems/evaluate-reverse-polish-notation/
if __name__ == "__main__":
    input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(input))
