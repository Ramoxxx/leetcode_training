"""
CHALLENGE 27

A text cleanup routine repeatedly removes any two adjacent identical
characters until no such pair remains. For example, "abbaca" loses the
"bb" to become "aaca", then loses the "aa" to become "ca".

Given the string, return the result after all possible adjacent pairs
have been removed.

Examples:
    squash("abbaca") -> "ca"
    squash("azxxzy") -> "ay"

Contract:
Comparison is case-sensitive; spaces and punctuation count as characters.
Empty input returns "". Remove pairs, not entire runs of any length.

"""

from testkit import check, report


def squash(text):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("cascading", squash("abbaca"), "ca")
    check("inner pair", squash("azxxzy"), "ay")
    check("all removed", squash("aabbcc"), "")
    check("nothing to remove", squash("abc"), "abc")
    check("empty", squash(""), "")
    check("single char", squash("a"), "a")
    check("odd run", squash("aaa"), "a")
    check('even run', squash("aaaa"), '')
    check('cascade to empty', squash("abccba"), '')
    check('case matters', squash("aA"), 'aA')
    report()
