"""
CHALLENGE 12

A support system scans an incoming message and wants the position of the
first character that appears only once in the whole message (useful for
spotting a unique marker). Return the index of the first non-repeating
character. If every character repeats, return -1.

Examples:
    first_unique("garden")  -> 0
    first_unique("levelup") -> 2

Contract:
Comparison is case-sensitive and spaces count as characters. Indices
start at 0. An empty message returns -1.

"""

from testkit import check, report


def first_unique(message):  
    seen_cpt = {}
    for char in message:        
        seen_cpt[char] = seen_cpt.get(char,0) + 1        
    for i,char in enumerate(message):
        if seen_cpt[char] < 2:
            return i
    return -1
        


if __name__ == "__main__":
    check("first char unique", first_unique("garden"), 0)
    check("unique later", first_unique("levelup"), 2)
    check("all repeat", first_unique("aabb"), -1)
    check("empty message", first_unique(""), -1)
    check("single char", first_unique("z"), 0)
    check("unique at end", first_unique("aabbc"), 4)
    check('spaces count', first_unique("aa "), 2)
    check('case matters', first_unique("aA"), 0)
    report()
