class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a1 = []
        

        for i in range(len(nums)//2):
            a1.append(nums[i])
            a1.append(nums[i+len(nums)//2])
        return a1
