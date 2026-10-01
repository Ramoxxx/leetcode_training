# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        currentNode = head
        while currentNode is not None and currentNode.next is not None:
            if(currentNode.val == currentNode.next.val):
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next       

        return head
param = ListNode(1,ListNode(1,ListNode(2,None)))
print("=====",Solution().deleteDuplicates(param),sep="\n",end="\n=====")
