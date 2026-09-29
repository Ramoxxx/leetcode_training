class Solution:
    def lengthOfLastWord(self, s: str) -> int:               
        index = len(s)-1
        while index >= 0 and s[index] == " ":
            index -= 1
        
        result = 0
        while index >= 0 and s[index] != " ":
            result += 1
            index -= 1
            
        return result
print(Solution().lengthOfLastWord("   fly me   to   the moon   "))
     
