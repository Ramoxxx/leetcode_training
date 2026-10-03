# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        pointer = 0
        while pointer < len(haystack):
            if haystack[pointer:].startswith(needle):
                return pointer
            pointer += 1        
        return -1