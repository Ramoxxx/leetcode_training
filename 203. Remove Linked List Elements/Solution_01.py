# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        node = head 
        result_head = ListNode(0,None) 
        current_result = result_head   
        while node:            
            if node.val != val:
                current_result.next = ListNode(node.val,None)                
                current_result = current_result.next

            node = node.next
           
        return result_head.next
        