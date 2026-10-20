"""
CHALLENGE 2

A moderation system flags two usernames as "suspiciously related" when
one is just a rearrangement of the other's characters (same letters,
same counts, possibly the same order). Given two usernames, return True if one
is a rearrangement of the other, otherwise False.

Comparison is exact (case matters, treat every character literally).

Examples:
    is_rearrangement("listen", "silent") -> True
    is_rearrangement("admin", "demon")   -> False

"""

from testkit import check, report


def is_rearrangement(a, b):
    occ_cpt_a = {}
    occ_cpt_b = {}
    for char in a:
        occ_cpt_a[char] = occ_cpt_a.get(char,0) + 1
    for char in b:
        occ_cpt_b[char] = occ_cpt_b.get(char,0) + 1
    return occ_cpt_a == occ_cpt_b        


if __name__ == "__main__":
    check("valid rearrangement", is_rearrangement("listen", "silent"), True)
    check("not related", is_rearrangement("admin", "demon"), False)
    check("different length", is_rearrangement("ab", "abc"), False)
    check("same letters different counts", is_rearrangement("aab", "abb"), False)
    check("case matters", is_rearrangement("a", "A"), False)
    check("identical", is_rearrangement("root", "root"), True)
    check("both empty", is_rearrangement("", ""), True)
    report()
