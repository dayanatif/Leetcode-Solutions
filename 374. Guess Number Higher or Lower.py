# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n

        while True:
            m = (l + r) // 2
            p = guess(m)

            if p > 0:
                l = m + 1
            elif p < 0:
                r = m - 1
            else:
                return m


        
