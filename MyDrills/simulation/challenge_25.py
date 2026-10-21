"""
CHALLENGE 25

A plagiarism checker scans a document for every spot where a window of
text uses the exact same letters (same counts) as a target keyword, in
any order. Given the document text and the keyword, return the starting
indices of every such window.

Return the indices in ascending order.

Examples:
    scramble_spots("cbaebabacd", "abc") -> [0, 6]
    scramble_spots("abab", "ab")        -> [0, 1, 2]

Contract:
Text and keyword contain lowercase English letters. The keyword is
non-empty; text may be empty. Match counts, not just the set of letters.
Indices start at 0; overlapping matches are included.

"""

from testkit import check, report


def scramble_spots(text, keyword):
    if len(text) < len(keyword):
        return []

    result = []
    kw_len = len(keyword)
    kw_occ_cpt = {}
    for char in keyword:
        kw_occ_cpt[char] = kw_occ_cpt.get(char,0) + 1
    win_occ_cpt = {}
    for i in range(0,kw_len):
        char = text[i]
        win_occ_cpt[char] = win_occ_cpt.get(char, 0) + 1
    win_is_valid = win_occ_cpt == kw_occ_cpt
    if win_is_valid:
        result.append(0)

    for i in range(1,len(text) - kw_len + 1):   
        enter = text[i + kw_len - 1]
        win_occ_cpt[enter] = win_occ_cpt.get(enter,0) + 1
        leave = text[i - 1]
        win_occ_cpt[leave] = win_occ_cpt.get(leave,0) - 1
        if win_occ_cpt[leave] < 1:
            win_occ_cpt.pop(leave)
        win_is_valid = win_occ_cpt == kw_occ_cpt
        if win_is_valid:
            result.append(i)
    
    return result
    


if __name__ == "__main__":
    check("two spots", scramble_spots("cbaebabacd", "abc"), [0, 6])
    check("overlapping", scramble_spots("abab", "ab"), [0, 1, 2])
    check("no match", scramble_spots("aa", "bb"), [])
    check("empty text", scramble_spots("", "a"), [])
    check("keyword too long", scramble_spots("a", "ab"), [])
    check("single spot", scramble_spots("baa", "aa"), [1])
    check('counts matter', scramble_spots("aababb", "aab"), [0, 1])
    check('single letter overlaps', scramble_spots("aaa", "a"), [0, 1, 2])
    report()
