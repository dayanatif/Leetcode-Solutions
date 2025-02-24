class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        res =[]
        for x in nums:
            if x in s:
                res.append(x)
            else:
                s.add(x)
        return res
