class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_d = {}

        for i, num in enumerate(nums):
            if num in num_d and i - num_d[num] <= k:
                return True
            num_d[num] = i 
        return False
