# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getval(root):
    if root.right == None and root.left == None:
        return root.val == 1
    
    left = getval(root.left)
    right = getval(root.right)

    if root.val == 3:
        return (left and right)
    elif root.val == 2:
        return (left or right)

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return getval(root)
