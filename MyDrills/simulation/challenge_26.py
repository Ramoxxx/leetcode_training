"""
CHALLENGE 26

A leaderboard is built from a list of operations applied to a running
list of scores. Each operation is one of:
    an integer string -> record that integer as a new score
    "+"               -> record a new score equal to the sum of the two
                         most recent scores
    "D"               -> record a new score equal to double the most
                         recent score
    "C"               -> remove (invalidate) the most recent score

Apply the operations in order and return the total of all scores that
remain recorded.

Examples:
    final_total(["5", "2", "C", "D", "+"])              -> 30
    final_total(["5", "-2", "4", "C", "D", "9", "+", "+"]) -> 27

Contract:
Every operation is valid: C and D have at least one preceding score,
and + has at least two. An empty operation list returns 0.

"""

from testkit import check, report


def final_total(ops):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("with cancel and double",
          final_total(["5", "2", "C", "D", "+"]), 30)
    check("longer sequence",
          final_total(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)
    check("single score", final_total(["1"]), 1)
    check("cancel to empty", final_total(["1", "C"]), 0)
    check("simple sum", final_total(["3", "6", "+"]), 18)
    check("no operations", final_total([]), 0)
    check('zero and negative', final_total(["0", "-3", "D", "+"]), -18)
    report()
