class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans =''
        for i in digits:
            ans+=str(i)
        b = int(ans)+1
        ans1 = []
        while b > 0:
            digit = b % 10
            ans1.append(digit)
            b = b // 10
        ans1.reverse()
        return ans1
        


        
