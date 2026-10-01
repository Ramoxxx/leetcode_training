# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        currentNode = head
        seen = set()
        while currentNode != None:  
            seen.add(currentNode.val)          
            next_found = False
            next_candidate = currentNode.next
            currentNode.next = None
            while not(next_found) and next_candidate != None:
                if next_candidate.val not in seen:
                    currentNode.next = next_candidate
                    next_found = True
                else:
                    next_candidate = next_candidate.next            
            currentNode = currentNode.next       

        return head
param = ListNode(1,ListNode(1,ListNode(2,None)))
print("=====",Solution().deleteDuplicates(param),sep="\n",end="\n=====")