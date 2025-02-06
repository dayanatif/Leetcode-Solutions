class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        original_num = num
        num = abs(num)
        remainders = []

        while num > 0:
            rem = num % 7
            remainders.append(str(rem))
            num //= 7

        if original_num < 0:
            remainders.append('-')
        remainders.reverse()
        return ''.join(remainders)
