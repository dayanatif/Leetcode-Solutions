class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers: i for s and j for t
        i = 0  # Pointer for s
        j = 0  # Pointer for t

        # Iterate over t, looking for characters from s in order
        while j < len(t) and i < len(s):
            if t[j] == s[i]:  # If we find a match, move pointer i in s
                i += 1
            # Always move pointer j in t
            j += 1

        # If we've matched all characters in s, i should equal len(s)
        return i == len(s)
