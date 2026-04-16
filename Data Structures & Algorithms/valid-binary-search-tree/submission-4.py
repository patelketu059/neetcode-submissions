# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return False

        def validBST(root, left, right):
            if not root: return True
            if not (left < root.val < right): return False
            return validBST(root.left, left, min(right, root.val)) and validBST(root.right, max(left, root.val), right)


        return validBST(root, float('-inf'), float('inf'))