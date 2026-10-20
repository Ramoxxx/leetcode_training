"""
CHALLENGE 4

A search box has an autocomplete feature. It suggests a full product
name only if the letters the user typed appear inside that name in the
same order (other letters may sit between them, but the order must
hold). Given the typed letters and a product name, return True if the
typed letters appear in order inside the name.

Examples:
    matches("abc", "aXbXXc") -> True
    matches("cab", "aXbXXc") -> False

Contract:
Comparison is case-sensitive. Both strings may be empty.

"""

from testkit import check, report


def matches(typed, name):
    if len(typed) <= 0: 
        return True      
    i_typed = 0
    for char in name:
        if char == typed[i_typed]:
            i_typed += 1
        if i_typed == len(typed):
            return True
    return i_typed == len(typed)


if __name__ == "__main__":
    check("letters in order", matches("abc", "aXbXXc"), True)
    check("wrong order", matches("cab", "aXbXXc"), False)
    check("nothing typed", matches("", "anything"), True)
    check("name too short", matches("ab", "a"), False)
    check("empty name", matches("a", ""), False)
    check("exact match", matches("abc", "abc"), True)
    check('both empty', matches("", ""), True)
    check('repeated letter needed', matches("aa", "a"), False)
    check('case matters', matches("A", "a"), False)
    report()
