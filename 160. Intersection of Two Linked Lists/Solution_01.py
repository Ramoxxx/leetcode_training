# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is headB:
            return headA
        node_a = headA       
        nodes_a_set = set()
        while node_a:
            nodes_a_set.add(node_a)
            node_a = node_a.next
        node_b = headB
        while node_b:
            if node_b in nodes_a_set:
                return node_b
            node_b = node_b.next
        return None