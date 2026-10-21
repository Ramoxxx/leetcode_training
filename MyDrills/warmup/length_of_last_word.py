"""
LENGTH OF LAST WORD
Pattern: String manipulation

Given a string made of words separated by spaces, return the length of
the last word. A word is a maximal substring of non-space characters.
There may be trailing spaces.

Examples:
    length_of_last_word("Hello World")        -> 5
    length_of_last_word("   fly me   to   the moon  ") -> 4
    length_of_last_word("luffy is still joyboy")       -> 6

Think about: trailing spaces can trip you up. How do you isolate the
words and grab the last one? Python string methods can help, but try
to reason about what they do.
Contract:
Input contains only English letters and ordinary spaces, with at least
one word. Empty strings and strings made only of spaces are out of scope.

"""

from testkit import check, report


def length_of_last_word(s):    
    s = s.strip()
    last_word = s.split(" ")[-1]
    return len(last_word)
    


if __name__ == "__main__":
    check("two words", length_of_last_word("Hello World"), 5)
    check("messy spacing", length_of_last_word("   fly me   to   the moon  "), 4)
    check("longer sentence", length_of_last_word("luffy is still joyboy"), 6)
    check("single word", length_of_last_word("word"), 4)
    check("trailing space only", length_of_last_word("a "), 1)
    check('leading spaces', length_of_last_word("   python"), 6)
    check('one letter', length_of_last_word("x"), 1)
    report()
