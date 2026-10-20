"""
CHALLENGE 9

An analytics dashboard shows the most viewed product IDs from a stream
of page views. Given the list of viewed product IDs and a number k,
return the k product IDs that appear most often.

To keep the output predictable, sort the result by frequency from
highest to lowest, breaking ties by smaller product ID first.

Examples:
    top_viewed([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
    top_viewed([4, 4, 4, 5, 5, 6, 6, 6, 6], 2) -> [6, 4]

Contract:
IDs are integers and 0 <= k <= the number of distinct IDs.
For k = 0, return []; views may then be empty.

"""

from testkit import check, report


def top_viewed(views, k):
    if k == 0:
        return []
    seen_cpt = {}    
    for view in views:
        seen_cpt[view] = seen_cpt.get(view,0) + 1
    result = sorted(seen_cpt,key=lambda x : (-seen_cpt[x],x))
    return result[:k]
        
    


if __name__ == "__main__":
    check("two most viewed", top_viewed([1, 1, 1, 2, 2, 3], 2), [1, 2])
    check("clear order", top_viewed([4, 4, 4, 5, 5, 6, 6, 6, 6], 2), [6, 4])
    check("single id", top_viewed([1], 1), [1])
    check("tie by value", top_viewed([1, 2], 2), [1, 2])
    check("tie picks smaller", top_viewed([7, 7, 3, 3, 1], 1), [3])
    check("k equals distinct", top_viewed([1, 1, 2, 2, 3], 3), [1, 2, 3])
    check("zero requested with views", top_viewed([1, 1, 2], 0), [])
    check("zero requested", top_viewed([], 0), [])
    check('negative tie breaker', top_viewed([-2, -2, 3, 3], 1), [-2])
    check('input order is not tie order', top_viewed([3, 2, 1], 2), [1, 2])
    report()
