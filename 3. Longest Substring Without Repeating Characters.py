class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        csets = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in csets:
                csets.remove(s[l])
                l += 1
            csets.add(s[r])
            res = max(res, r-l+1)
        return res

        
