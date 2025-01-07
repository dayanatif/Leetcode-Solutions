class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        final=[]
        for i in range(len(nums)):
            b = nums[i]**2
            final. append(b)

        final.sort()
        return final
        
