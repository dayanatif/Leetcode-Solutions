class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        while len(nums) > 0:
            alice = nums.pop(0)
            bib = nums.pop(0)
            arr.append(bib)
            arr.append(alice)
        return arr
        
        


        
