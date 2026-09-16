class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {")":"(","}":"{","]":"["}

        for i in s:
            if i in closedToOpen:
                if not stack or stack[-1] != closedToOpen[i]:
                    return False

                stack.pop()

            else:
                stack.append(i)

        return len(stack) == 0
                
           