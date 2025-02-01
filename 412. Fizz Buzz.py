class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        i = 'FizzBuzz'
        j = 'Fizz'
        k = 'Buzz'
        

        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 == 0:
                answer.append(i)
            elif num % 3 == 0:
                answer.append(j)
            elif num % 5 == 0:
                answer.append(k)
            else:
                answer.append(str(num))
        return answer
