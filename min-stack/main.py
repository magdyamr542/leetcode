class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            topMin = self.minStack[len(self.minStack) - 1]
            self.minStack.append(min(val , topMin ))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
        
        
    
    

# https://leetcode.com/problems/min-stack/
if __name__ == "__main__":
    pass
