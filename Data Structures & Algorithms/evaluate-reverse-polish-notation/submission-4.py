class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                right = stack.pop()
                left = stack.pop()
                if tokens[i] == "+":
                    val = left+right 
                elif tokens[i] == "-":
                    val = left-right 
                elif tokens[i] == "*":
                    val = left*right 
                else:
                    val = int(left/right)
                
                stack.append(val)

        return stack.pop()