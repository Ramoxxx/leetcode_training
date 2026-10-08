class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenCpt = dict()
        seenIndexes = dict()
        for i,char in enumerate(s):
            seenCpt[char] = seenCpt.get(char,0) + 1
            if not char in seenIndexes.keys():
               seenIndexes[char] = i  
        for char in seenCpt.keys():
            if seenCpt[char] == 1:
                return seenIndexes[char]
        return -1