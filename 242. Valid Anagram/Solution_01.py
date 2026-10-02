class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur_s = dict()
        occur_t = dict()
        for letter in s:
            occur_s[letter] = occur_s.get(letter,0) + 1
        for letter in t:
            occur_t[letter] = occur_t.get(letter,0) + 1

        return occur_s == occur_t