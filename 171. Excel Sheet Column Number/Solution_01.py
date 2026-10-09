class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total = 0
        for char in columnTitle:
            val = letters.index(char)+1
            total = total * 26 + val
            
        return total