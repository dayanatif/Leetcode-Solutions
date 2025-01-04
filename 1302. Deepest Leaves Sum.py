# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0

        while q:
            res = 0
            for _ in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    res += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
