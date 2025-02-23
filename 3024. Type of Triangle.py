class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort the sides to make the comparison easier
        nums.sort()
        
        # Check if it forms a triangle
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        
        # Check for triangle types
        if nums[0] == nums[1] == nums[2]:
            return 'equilateral'
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return 'isosceles'
        else:
            return 'scalene'
