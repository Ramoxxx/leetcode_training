"""
DUPLICATE ENCODER
Pattern: HashMap frequency

Convert a string into a new string where each character is replaced by
"(" if it appears only once in the original string, or ")" if it
appears more than once. The check is case-insensitive and spaces count
as characters too.

Examples:
    duplicate_encode("din")    -> "((("
    duplicate_encode("recede") -> "()()()"
    duplicate_encode("Success") -> ")())())"
    duplicate_encode("(( @")    -> "))(("

Think about: you need to know each character's total count BEFORE you
start building the answer. So make one pass to count, then a second
pass to build the output.
Contract:
Input is an ASCII string and may be empty. Return a string.

"""

from testkit import check, report


def duplicate_encode(word):
    word = word.lower()
    seen_cpt = {}
    result = [""] * len(word)
    for char in word:
        seen_cpt[char] = seen_cpt.get(char,0) + 1
    for i in range(0,len(word)):
        result[i] = "(" if seen_cpt.get(word[i]) < 2 else ")"
    return "".join(result)
    


if __name__ == "__main__":
    check("all unique", duplicate_encode("din"), "(((")
    check("mixed frequencies", duplicate_encode("recede"), "()()()")
    check("case insensitive", duplicate_encode("Success"), ")())())")
    check("symbols and spaces", duplicate_encode("(( @"), "))((")
    check("empty string", duplicate_encode(""), "")
    check('same letter different case', duplicate_encode("aA"), '))')
    check('single space', duplicate_encode(" "), '(')
    check('all repeated', duplicate_encode("aaaa"), '))))')
    report()
