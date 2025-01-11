class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sum1 =""
        for i in range(len(word1)):
            sum1 += word1[i]
        sum2 =""
        for j in range(len(word2)):
            sum2 += word2[j]
        if sum1 == sum2:
            return True
        else:
            return False

        
