# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        right = [root.val]
        q = deque([root])
        while q:
            layer = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    layer.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    layer.append(node.right.val)
                    q.append(node.right)


            if layer: right.append(layer[-1])

        return right