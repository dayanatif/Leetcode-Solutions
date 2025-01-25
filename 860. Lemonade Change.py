class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = 0
        c10 = 0
        
        for i in bills:
            if i == 5:
                c5 += 1
            if i == 10:
                c10 += 1
            change = i - 5
            if change == 5:
                if c5 > 0:
                    c5 -= 1
                else:
                    return False
            elif change == 15:
                if c5 > 0 and c10 > 0:
                    c5 -= 1
                    c10 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False
        return True
                   

        class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = 0
        c10 = 0
        
        for i in bills:
            if i == 5:
                c5 += 1
            if i == 10:
                c10 += 1
            change = i - 5
            if change == 5:
                if c5 > 0:
                    c5 -= 1
                else:
                    return False
            elif change == 15:
                if c5 > 0 and c10 > 0:
                    c5 -= 1
                    c10 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False
        return True
                   

        
