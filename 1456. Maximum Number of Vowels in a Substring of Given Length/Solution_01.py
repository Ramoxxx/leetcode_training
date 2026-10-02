# TimeoutError, should rather check if left is vowel then add (and same with right substract)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        left = 0
        right = k
        max_vowels = 0
        while right <= len(s):
            sub_str = s[left:right]
            sub_str_vowels = 0
            for char in sub_str:
                if char in vowels:
                   sub_str_vowels += 1
            max_vowels = max(max_vowels, sub_str_vowels)                           
            left += 1
            right += 1
        return max_vowels