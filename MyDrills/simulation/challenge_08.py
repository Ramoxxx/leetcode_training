"""
CHALLENGE 8

A catalog tool wants to cluster product codes that are built from the
exact same letters, possibly in a different order (same letters, same
counts). Given a list of product codes, group together the ones that are
rearrangements of each other.

To keep the output predictable, return a list of groups where each group
is sorted alphabetically, and the groups themselves are sorted by their
first element.

Examples:
    cluster(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    cluster(["abc", "bca", "xyz"])
        -> [["abc", "bca"], ["xyz"]]

Contract:
Codes are strings; comparison is case-sensitive. Empty codes and an
empty list are allowed. Keep repeated codes in the output.

"""

from testkit import check, report


def cluster(codes):
    combis = {}
    result = []
    
    for code in codes:
        sorted_code = "".join(sorted(code))
        if not sorted_code in combis:
            combis[sorted_code] = []
        combis[sorted_code].append(code)
    for combi in combis.values():
        combi.sort()
        result.append(combi)
    result.sort()
    return result
        
        


if __name__ == "__main__":
    check("classic groups",
          cluster(["eat", "tea", "tan", "ate", "nat", "bat"]),
          [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    check("two groups",
          cluster(["abc", "bca", "xyz"]),
          [["abc", "bca"], ["xyz"]])
    check("empty input", cluster([]), [])
    check("single empty string", cluster([""]), [[""]])
    check("single code", cluster(["a"]), [["a"]])
    check("duplicates kept",
          cluster(["ab", "ba", "ab"]),
          [["ab", "ab", "ba"]])
    check('same letters different counts', cluster(["aab", "abb", "aba"]), [['aab', 'aba'], ['abb']])
    check('empty codes kept', cluster(["", ""]), [['', '']])
    check('case matters', cluster(["a", "A"]), [['A'], ['a']])
    report()
