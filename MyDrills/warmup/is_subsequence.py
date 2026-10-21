"""
IS SUBSEQUENCE
Pattern: Two Pointers

Given two strings `s` and `t`, return True if `s` is a subsequence of
`t`. A subsequence keeps the characters in order but may skip some.
You do NOT rearrange characters.

Examples:
    is_subsequence("abc", "ahbgdc") -> True
    is_subsequence("axc", "ahbgdc") -> False

Think about: walk through `t` with one pointer. Keep a second pointer
on `s`. Every time the current character of `t` matches the character
`s` is waiting for, advance the `s` pointer. Did `s` reach the end?
Contract:
Comparison is case-sensitive; both strings may be empty. Return a bool.

"""

from testkit import check, report


def is_subsequence(s, t):    
    if len(s) == 0:
        return True
    len_to_find = len(s)
    index_s = 0
    for letter in t:
        if letter == s[index_s]:            
            index_s += 1
        if index_s == len_to_find:
            return True
    return False


if __name__ == "__main__":
    check("is a subsequence", is_subsequence("abc", "ahbgdc"), True)
    check("not a subsequence", is_subsequence("axc", "ahbgdc"), False)
    check("empty s", is_subsequence("", "anything"), True)
    check("empty t", is_subsequence("a", ""), False)
    check("equal strings", is_subsequence("abc", "abc"), True)
    check("order matters", is_subsequence("ba", "ab"), False)
    check('both empty', is_subsequence("", ""), True)
    check('cannot reuse one character', is_subsequence("aa", "a"), False)
    check('case sensitive', is_subsequence("A", "a"), False)
    report()
