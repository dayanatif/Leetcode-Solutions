class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(1,len(s)):
            count = count + abs(ord(s[i-1])-ord(s[i]))
        return count
