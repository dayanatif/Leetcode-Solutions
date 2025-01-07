class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        #primary
        row = 0
        col = 0
        sum = 0
        while row < len(mat) and col < len(mat):
            sum = sum + mat[row][col]
            row+=1
            col+=1
        
        #secondary
        row = 0
        col = len(mat) - 1
        while row < len(mat) and col >= 0:
            sum = sum + mat[row][col]
            row+=1
            col-=1

        if len(mat)%2!=0:
            row = len(mat)//2
            col = len(mat)//2
            sum = sum - mat[row][col]
            
        return sum
        
