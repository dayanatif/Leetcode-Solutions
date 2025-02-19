class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for i in counter.values():
            if i > 2:
                return False
        return True
