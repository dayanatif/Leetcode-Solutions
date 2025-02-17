# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def getleaf(root,result):
            if root.left is None and root.right is None:
                result.append(root.val)
            if root.left:
                getleaf(root.left,result)
            if root.right:
                getleaf(root.right,result)
            return

        getleaf(root1,leaf1)
        getleaf(root2,leaf2)

        if leaf1 == leaf2:
            return True
        else:
            return False
