"""
CHALLENGE 5

A configuration language uses three kinds of brackets to open and close
blocks: ( ), [ ], and { }. A configuration string is well-formed only
if every block that opens is closed by the matching bracket, and blocks
are closed in the reverse order they were opened. Given such a string
(containing only bracket characters), return True if it is well-formed.

Examples:
    well_formed("{[()]}")  -> True
    well_formed("{[(])}")  -> False
    well_formed("(()")     -> False

Contract:
The empty configuration is well-formed. Return a bool.

"""

from testkit import check, report


def well_formed(config):
    corr = {
        "]":"[",
        "}":"{",
        ")":"("
    }
    stack = []
    for char in config:
        if char in corr:
            if not stack or stack.pop() != corr[char]:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    check("nested ok", well_formed("{[()]}"), True)
    check("crossed", well_formed("{[(])}"), False)
    check("unclosed", well_formed("(()"), False)
    check("empty", well_formed(""), True)
    check("flat sequence", well_formed("()[]{}"), True)
    check("lone closer", well_formed("]"), False)
    check('opens without closes', well_formed("([{"), False)
    check('close before open', well_formed(")("), False)
    report()
