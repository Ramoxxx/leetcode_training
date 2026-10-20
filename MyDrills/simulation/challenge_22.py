"""
CHALLENGE 22

A data-masking tool replaces characters in a token with other characters.
Two tokens are "structurally equal" if one can be turned into the other
by a consistent one-to-one replacement: every occurrence of a character
maps to the same character, and no two different characters map to the
same one.

Given two tokens, return True if they are structurally equal, otherwise
False. Tokens of different lengths are never structurally equal.

Examples:
    same_shape("egg", "add")     -> True
    same_shape("foo", "bar")     -> False

Contract:
Comparison is case-sensitive and every character counts.
A character may map to itself. Two empty tokens return True.

"""

from testkit import check, report


def same_shape(a, b):
    if len(a) != len(b):
        return False
    
    forward = {}
    backward = {}
    
    for i,char in enumerate(a):
        
        if char in forward and forward[char] != b[i] or b[i] in backward and backward[b[i]] != char:
            return False   
        
        forward[char] = b[i]
        backward[b[i]] = char
        
    
    return True


if __name__ == "__main__":
    check("matching shape", same_shape("egg", "add"), True)
    check("conflict", same_shape("foo", "bar"), False)
    check("paper title", same_shape("paper", "title"), True)
    check("not bijective", same_shape("badc", "baba"), False)
    check("different lengths", same_shape("ab", "a"), False)
    check("both empty", same_shape("", ""), True)
    check("collapse", same_shape("ab", "aa"), False)
    check("single char", same_shape("a", "z"), True)
    check('self mapping', same_shape("abc", "abc"), True)
    check('reverse length mismatch', same_shape("a", "ab"), False)
    report()
