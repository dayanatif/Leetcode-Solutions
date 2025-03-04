class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxl = 0

        for num in nums:
            if num-1 not in num_set:
                curnum = num
                curlen = 1

                while curnum+1 in num_set:
                    curlen += 1
                    curnum += 1
                maxl = max(maxl,curlen)
        return maxl
