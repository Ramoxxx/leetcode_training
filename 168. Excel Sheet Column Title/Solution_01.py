class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        stack = list()
        while columnNumber > 0:
            columnNumber -= 1
            stack.append(letters[columnNumber % 26])
            columnNumber //= 26
        stack.reverse()
        return "".join(stack)