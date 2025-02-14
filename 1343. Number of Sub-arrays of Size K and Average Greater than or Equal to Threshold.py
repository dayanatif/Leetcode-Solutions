class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cursum = sum(arr[:k])

        count = 0

        if cursum / k >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            cursum = cursum + arr[i] - arr[i - k]

            if cursum / k >= threshold:
                count += 1
        return count

