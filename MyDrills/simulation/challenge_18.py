"""
CHALLENGE 18

A file browser groups uploaded files by the longest character prefix they
all share (not a directory path). Given a list of file names, return the longest starting string
that every name begins with. If they share no common start, return the
empty string.

Examples:
    common_start(["flower", "flow", "flight"]) -> "fl"
    common_start(["dog", "racecar", "car"])    -> ""

Contract:
Comparison is case-sensitive and character by character.
An empty list returns "".

"""

from testkit import check, report

def common_start(names):
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0]
    index = 0
    result = []
    while True:
        if index >= len(names[0]):
            return "".join(result)
        current_char = names[0][index]
        for i in range(1,len(names)):
            name = names[i]
            if index >= len(name) or name[index] != current_char:
                return "".join(result)
        result.append(current_char)     
        index += 1

if __name__ == "__main__":
    check("shared prefix", common_start(["flower", "flow", "flight"]), "fl")
    check("nothing shared", common_start(["dog", "racecar", "car"]), "")
    check("long prefix",
          common_start(["interspecies", "interstellar", "interstate"]),
          "inters")
    check("single name", common_start(["alone"]), "alone")
    check("empty list", common_start([]), "")
    check("identical names", common_start(["same", "same"]), "same")
    check("contains empty", common_start(["abc", ""]), "")
    check('prefix ends inside a name', common_start(["ab", "abc"]), 'ab')
    check('case matters', common_start(["Ab", "ab"]), '')
    report()
