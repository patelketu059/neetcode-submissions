# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def DFS(root):
            if not root: return 
            left = DFS(root.left)
            if left is not None: return left
            self.count += 1
            if self.count == k: return root.val

            right = DFS(root.right)
            if right is not None: return right 
        
        return DFS(root)
        


