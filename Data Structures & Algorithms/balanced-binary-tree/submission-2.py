# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(i):
            if not i: return 0            
            L = dfs(i.left)
            R = dfs(i.right)
            print(i, L, R)
            if L == -1 or R == -1: return -1

            if abs(R - L) > 1:
                return -1
            else:
                return 1 + max(R, L)

        
        return False if dfs(root) == -1 else True