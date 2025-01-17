class Solution(object):
    def finalString(self, s):
        
        s1 = ""
        for w in s:
            if w == "i":
                s1 = s1[::-1]
            else:
                s1+=w
        return s1  
