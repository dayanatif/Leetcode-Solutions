class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0,1,1]
        for i in range(3,n+1):
            seq.append(seq[i-3]+seq[i-2]+seq[i-1])
        return seq[n]
