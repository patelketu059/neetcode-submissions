# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_val = root.val

        def dfs(node):
            if not node: return 0

            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            self.max_val = max(self.max_val, left_val + right_val + node.val)

            return max(left_val, right_val) + node.val

        dfs(root)
        return self.max_val
        