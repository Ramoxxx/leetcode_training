"""
STRING MERGE
Pattern: Strings / parallel traversal

The input contains two equally long, non-empty alphanumeric strings
separated by exactly one "*". Return their characters interleaved,
starting with the first character of the left string. Omit the "*".

Examples:
    string_merge("abc1*kyoo") -> "akbyco1o"
    string_merge("aaa*bbb")   -> "ababab"
    string_merge("A*9")       -> "A9"

Contract: the format and equal lengths are guaranteed. Preserve case.
You do not need to validate malformed input or handle unequal lengths.

Think about: split once, then pair characters at matching indices.

Source: recueil_questions.md, Coderbyte String Merge.
"""

from testkit import check, report


def string_merge(text):
    result = []
    splitted = text.split("*")
    left_part = splitted[0]
    right_part = splitted[1]
    for i in range(len(left_part)):
        result += [left_part[i],right_part[i]]
    return "".join(result)
        


if __name__ == "__main__":
    check("letters and digits", string_merge("abc1*kyoo"), "akbyco1o")
    check("repeated letters", string_merge("aaa*bbb"), "ababab")
    check("single pair", string_merge("A*9"), "A9")
    check("preserve case", string_merge("Ab*Cd"), "ACbd")
    check("digits stay strings", string_merge("12*34"), "1324")
    check("longer halves", string_merge("123hg*aaabb"), "1a2a3ahbgb")
    report()
