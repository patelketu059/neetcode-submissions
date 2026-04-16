# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        stack = [[root.val]]

        while q:
            layer = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    layer.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    layer.append(node.right.val)
                
            stack.append(layer)
        
        return stack[:-1]
        