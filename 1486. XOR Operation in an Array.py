class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = [start]
        count = start
        for i in range(1,n):
            l.append(start + 2*i)
            count^= l[-1]
        return count
                
