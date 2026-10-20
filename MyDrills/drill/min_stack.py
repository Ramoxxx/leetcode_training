"""
MIN STACK
Pattern: Stack design (track auxiliary state)

Design a stack that supports push, pop, top, and retrieving the minimum
element, all in O(1) time. Implement the class below.

    push(x)    add x on top
    pop()      remove the top element
    top()      return the top element (do not remove)
    get_min()  return the smallest element currently in the stack

Example:
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    s.get_min()  -> -3
    s.pop()
    s.top()      -> 0
    s.get_min()  -> -2

Think about: get_min must be O(1), so you cannot scan the stack each
time. What if you keep a SECOND stack that always knows the minimum so
far? When you pop the main stack, keep the two in sync.
Contract:
Values are integers. pop() removes an element and returns None; push()
also returns None. pop(), top(), and get_min() are only called on a
non-empty stack. Separate instances must have independent state.

"""

from testkit import check, report


class MinStack:
    def __init__(self):
        pass

    def push(self, x):
        # TODO
        pass

    def pop(self):
        # TODO
        pass

    def top(self):
        # TODO
        pass

    def get_min(self):
        # TODO
        pass


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    check("min after three pushes", s.get_min(), -3)
    s.pop()
    check("top after one pop", s.top(), 0)
    check("min after one pop", s.get_min(), -2)

    s2 = MinStack()
    s2.push(5)
    check("single element top", s2.top(), 5)
    check("single element min", s2.get_min(), 5)
    s2.push(3)
    s2.push(3)
    s2.pop()
    check("min with equal values", s2.get_min(), 3)
    s2.pop()
    check("min restored after duplicate minima removed", s2.get_min(), 5)
    check("other instance unchanged", s.get_min(), -2)
    check("pop returns None", s2.pop(), None)
    check("push after empty returns None", s2.push(9), None)
    check("minimum after reuse", s2.get_min(), 9)
    check("top does not remove", s2.top(), 9)
    check("top still present", s2.top(), 9)
    s2.push(10)
    check("increasing push keeps minimum", s2.get_min(), 9)
    report()
