class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None or list2 is None:
            return None
        result = list1 if list1.val < list2.val else list2
        other = list2 if result is list1 else list1
        while result != None:
            if other != None:
                if result.next.val >= other.next.val:
                    result.next.next = other.next
Solution().mergeTwoLists(ListNode(),ListNode())      

        