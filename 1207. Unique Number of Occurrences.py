class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        return True if len(set(counts.values())) == len(counts.values()) else False
