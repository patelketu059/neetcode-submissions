# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q: return True
        # if not p or not q: return False

        def dfs(T1, T2):
            if not T1 and not T2: return True
            if T1 and T2 and T1.val != T2.val: return False
            if not T1 or not T2: return False

            return dfs(T1.left, T2.left) and dfs(T1.right, T2.right)

        return dfs(p, q)

