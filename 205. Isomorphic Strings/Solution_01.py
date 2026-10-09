class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        remapped1 = dict()
        remapped2 = dict()
        for i in range(0,len(s)):
            char1 = s[i]
            char2 = t[i]

            if not char1 in remapped1.keys():
                remapped1[char1] = char2
            if not char2 in remapped2.keys():
                remapped2[char2] = char1
            
            if remapped1[char1] != char2 or remapped2[char2] != char1:
                return False

        return True    
        
        