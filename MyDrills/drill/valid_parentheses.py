"""
VALID PARENTHESES
Pattern: Stack

Given a string containing only the characters ( ) [ ] { }, return True
if every opening bracket is closed by a matching bracket in the correct
order, otherwise False.

Examples:
    is_valid("()")     -> True
    is_valid("()[]{}") -> True
    is_valid("(]")     -> False
    is_valid("([)]")   -> False
    is_valid("{[]}")   -> True

Think about: a closing bracket must match the MOST RECENT unmatched
opening bracket. "Most recent" is the clue: which data structure gives
you back the last thing you put in?
Contract:
The empty string is valid. Return a bool.

"""

from testkit import check, report


def is_valid(s):
    corr = {
        "]":"[",
        ")":"(",
        "}":"{",
    }
    stack = []
    for i,char in enumerate(s):        
        if char in corr:
            if not stack or stack.pop() != corr.get(char):
                return False
        else:            
            stack.append(char)
    return not stack


if __name__ == "__main__":
    check("simple pair", is_valid("()"), True)
    check("all three types", is_valid("()[]{}"), True)
    check("wrong close", is_valid("(]"), False)
    check("interleaved wrong", is_valid("([)]"), False)
    check("nested correct", is_valid("{[]}"), True)
    check("empty string", is_valid(""), True)
    check("only opening", is_valid("((("), False)
    check("only closing", is_valid(")"), False)
    report()
