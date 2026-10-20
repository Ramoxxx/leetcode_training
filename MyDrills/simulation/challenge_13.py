"""
CHALLENGE 13

A spreadsheet column lists daily sales figures, but the days with no
sales (zeros) should be pushed to the bottom of the column while keeping
every non-zero figure in its original order. Modify the list so all
zeros sit at the end, and return the list.

Examples:
    sink_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
    sink_zeros([4, 0, 5, 0, 0, 6]) -> [4, 5, 6, 0, 0, 0]

Contract:
Figures are integers and may be negative. Empty lists are allowed.
Modify the original list in place and return that same list object.

"""

from testkit import check, report


def sink_zeros(figures):
    result_i = 0
    for i,figure in enumerate(figures):
        if figure != 0:
            figures[result_i] = figure
            result_i += 1
    for i in range(result_i, len(figures)):
        figures[i] = 0
    return figures


if __name__ == "__main__":
    check("mixed", sink_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
    check("several zeros", sink_zeros([4, 0, 5, 0, 0, 6]), [4, 5, 6, 0, 0, 0])
    check("all zeros", sink_zeros([0, 0, 0]), [0, 0, 0])
    check("no zeros", sink_zeros([1, 2, 3]), [1, 2, 3])
    check("empty", sink_zeros([]), [])
    check("single zero", sink_zeros([0]), [0])
    check('negative figures keep order', sink_zeros([0, -2, 3, 0, -1]), [-2, 3, -1, 0, 0])
    original = [0, 1, 0, -2]
    result = sink_zeros(original)
    check("original list modified", original, [1, -2, 0, 0])
    check("same list returned", result is original, True)
    report()
