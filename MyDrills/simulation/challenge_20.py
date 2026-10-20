"""
CHALLENGE 20

A search bar normalizes a query by reversing the order of the words and
collapsing whitespace: leading and trailing spaces are dropped, and any
run of spaces between words becomes a single space.

Given the raw query, return the cleaned, word-reversed string.

Examples:
    reverse_words("the sky is blue") -> "blue is sky the"
    reverse_words("  hello world  ") -> "world hello"

Contract:
Whitespace includes spaces, tabs, and newlines. Empty input or input
containing only whitespace returns "".

"""

from testkit import check, report


def reverse_words(query):
    words = query.split()    
    words.reverse()
    return " ".join(words)


if __name__ == "__main__":
    check("clean input", reverse_words("the sky is blue"), "blue is sky the")
    check("trim ends", reverse_words("  hello world  "), "world hello")
    check("inner spaces", reverse_words("a good   example"), "example good a")
    check("single word", reverse_words("single"), "single")
    check("only spaces", reverse_words("   "), "")
    check("empty", reverse_words(""), "")
    check('tabs and newlines', reverse_words("one\ttwo\nthree"), 'three two one')
    report()
