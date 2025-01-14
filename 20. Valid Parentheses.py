class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {"}":"{",")":"(","]":"["}

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack:
                    if mapping[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) ==0:
            return True
        else:
            return False
        
