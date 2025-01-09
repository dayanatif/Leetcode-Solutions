class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            c=0
            for j in range(len(accounts[i])):
                c+=accounts[i][j]
            if c >= max_wealth:
                max_wealth = c
        return max_wealth
