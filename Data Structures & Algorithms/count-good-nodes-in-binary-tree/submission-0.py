# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        def countGood(root, max_val):
            if not root: return 
            if root.val >= max_val: self.count += 1
            max_val = max(max_val, root.val)
            if root.left: countGood(root.left, max_val)
            if root.right: countGood(root.right, max_val)
            return 

        countGood(root, root.val)
        return self.count