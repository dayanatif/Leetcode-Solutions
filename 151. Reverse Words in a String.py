class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        revwords = words[::-1]
        return ' '.join(revwords)
