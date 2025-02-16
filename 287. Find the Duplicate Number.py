class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()

        for i in range(len(nums)):
            if nums[i] in s:
                return nums[i]
            else:
                s.add(nums[i])
