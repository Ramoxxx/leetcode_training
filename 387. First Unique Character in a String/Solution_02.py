class Solution:
    def firstUniqChar(self, s: str) -> int:

        seenCpt = dict()
        for char in s:
            seenCpt[char] = seenCpt.get(char,0) + 1
        for i,char in enumerate(s):
            if seenCpt[char] == 1:
                return i
        return -1