
def decodeString(s: str):
    stack = []
    for char in s:
        if char != "]":
            stack.append(char)
        else:
            currStr = ""
            while stack[-1] != "[":
                currStr = stack[-1] + currStr
                stack.pop()

            stack.pop() # remove the "["

            # get the num
            currNum = ""
            while stack and stack[-1].isdigit():
                currNum = stack[-1] + currNum
                stack.pop()

            stack.append(int(currNum) * currStr)

    return "".join(stack)

                
#https://leetcode.com/problems/decode-string/
if __name__ == "__main__":
    print(decodeString("cf1[2[abab]]"))



    
