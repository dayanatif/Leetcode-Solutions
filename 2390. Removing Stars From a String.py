class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        my_str = ''.join(stack)
        return my_str
        
