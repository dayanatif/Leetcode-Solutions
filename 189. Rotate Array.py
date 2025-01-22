class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = [0] * n

        for i in range(n):
            temp[(i+k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = temp[i]
        
        return nums
