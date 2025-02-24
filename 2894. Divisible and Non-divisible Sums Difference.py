class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a1 = []
        a2 = []

        for i in range(1,n+1):
            if i % m !=0:
                a1.append(i)
            else:
                a2.append(i)

        return sum(a1) - sum(a2)
