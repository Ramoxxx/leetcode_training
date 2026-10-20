"""
VALID PALINDROME
Pattern: Two Pointers

A phrase is a palindrome if, after lowercasing and removing every
character that is not a letter or digit, it reads the same forward and
backward. Return True if the input is a palindrome, otherwise False.

Examples:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("race a car")                     -> False
    is_palindrome(" ")                              -> True

Think about: you could clean the string first, then compare it to its
reverse. The two-pointer version is nicer: one pointer from the left,
one from the right, skip non-alphanumeric characters, compare as you
move inward.
Contract:
Input is ASCII and may be empty. Only a-z, A-Z, and 0-9 are retained.

"""

from testkit import check, report


def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left +=1
        right -= 1
    return True


if __name__ == "__main__":
    check("classic palindrome", is_palindrome("A man, a plan, a canal: Panama"), True)
    check("not a palindrome", is_palindrome("race a car"), False)
    check("only punctuation", is_palindrome(" "), True)
    check("single letter", is_palindrome("a"), True)
    check("alphanumeric mix", is_palindrome("0P"), False)
    check("digits palindrome", is_palindrome("12321"), True)
    check('empty', is_palindrome(""), True)
    check('punctuation ignored', is_palindrome(".,!?"), True)
    report()
