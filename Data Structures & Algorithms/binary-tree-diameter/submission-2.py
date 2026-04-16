# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        D = 0

        def dfs(i):
            nonlocal D 

            if not i: return 0
            L = dfs(i.left)
            R = dfs(i.right)

            H = 1 + max(L, R)
            D = max(D, L + R)
            return H
        
        dfs(root)
        return D