# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = node = ListNode()
        node = head

        visited = dict()
        while node:
            if node in visited:
                return True
            visited[node] = node.val
            node = node.next

        return False