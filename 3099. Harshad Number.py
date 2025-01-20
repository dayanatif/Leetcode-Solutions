class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0

        num = str(x)

        for i in num:
            sum = sum + int(i)
        
        if x % sum ==0:
            return sum
        else:
            return -1
