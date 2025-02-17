# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        
        #recursive case
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
        
