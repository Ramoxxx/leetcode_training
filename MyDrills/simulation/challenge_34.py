"""
CHALLENGE 34

A list of ticket numbers was originally sorted in ascending order with no
repeats, but the stack was then rotated at some unknown point (the front
chunk was moved to the back). For example, [0,1,2,4,5,6,7] might become
[4,5,6,7,0,1,2]. Given such a rotated list and a target ticket number,
return its index, or -1 if it is not present.

Examples:
    locate([4, 5, 6, 7, 0, 1, 2], 0) -> 4
    locate([4, 5, 6, 7, 0, 1, 2], 3) -> -1

Contract:
Tickets and target are integers. The list may be empty or not rotated.
Required time: O(log n).

"""

from testkit import check, report


def locate(tickets, target):
    left = 0
    right = len(tickets) - 1

    while left <= right:
        mid = (left + right) // 2
        if tickets[mid] == target:
            return mid
        if tickets[mid] >= tickets[left]: # left is sorted
            if target >= tickets[left] and target <= tickets[mid]: # target is in left part
                right = mid - 1
            else:
                left = mid + 1
        else: # left is not sorted, right must be sorted
            if target >= tickets[mid] and target <= tickets[right]:
                left = mid + 1
            else:
                right = mid - 1


    
    return - 1


if __name__ == "__main__":
    check("found in tail", locate([4, 5, 6, 7, 0, 1, 2], 0), 4)
    check("not present", locate([4, 5, 6, 7, 0, 1, 2], 3), -1)
    check("found in head", locate([4, 5, 6, 7, 0, 1, 2], 5), 1)
    check("single miss", locate([1], 0), -1)
    check("single hit", locate([1], 1), 0)
    check("empty", locate([], 5), -1)
    check("small rotation", locate([5, 1, 3], 5), 0)
    check("not rotated", locate([1, 2, 3, 4], 3), 2)
    check('two rotated first', locate([2, 1], 2), 0)
    check('two rotated second', locate([2, 1], 1), 1)
    check('pivot is smallest', locate([3, 4, 1, 2], 1), 2)
    report()
