"""
VALID ANAGRAM
Pattern: HashMap (character frequency)

Two strings are anagrams if they contain exactly the same characters
with the same counts, just in a different order.

Write a function that returns True if `t` is an anagram of `s`,
otherwise False.

Examples:
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car")         -> False

Think about: how do you compare the contents of two strings while
ignoring the order? What data structure counts things for you?
Contract:
Comparison is case-sensitive and every character counts, including spaces.
Empty strings are allowed. Return a bool.

"""

from testkit import check, report


def is_anagram(s, t):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("classic anagram", is_anagram("anagram", "nagaram"), True)
    check("not an anagram", is_anagram("rat", "car"), False)
    check("different lengths", is_anagram("a", "ab"), False)
    check("both empty", is_anagram("", ""), True)
    check("same letters repeated", is_anagram("aacc", "ccac"), False)
    check("single char match", is_anagram("z", "z"), True)
    check('case matters', is_anagram("A", "a"), False)
    check('spaces count', is_anagram("a ", " a"), True)
    check('positive repeated counts', is_anagram("aabb", "baba"), True)
    report()
