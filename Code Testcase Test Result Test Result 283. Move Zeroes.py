class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        track = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[track],nums[i] = nums[i],nums[track]
                track+=1
        return nums        
