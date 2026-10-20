"""
CHALLENGE 11

After an online poll, every vote is a candidate ID. One candidate won by
a strict majority, meaning their ID appears more than half the time in
the list of votes. Return the winning candidate ID.

You may assume such a majority always exists.

Examples:
    winner([3, 2, 3])             -> 3
    winner([2, 2, 1, 1, 1, 2, 2]) -> 2

Contract:
Votes are integers and the list is non-empty.

"""

from testkit import check, report


def winner(votes):
    candidate = None
    cpt = 0
    for id in votes:
        if cpt == 0:
            candidate = id
        if id == candidate:
            cpt += 1
        else:
            cpt -= 1
    return candidate        
    # total_votes = len(votes)
    # occ_cpt = {}
    # for id in votes:
    #     occ_cpt[id] = occ_cpt.get(id,0) + 1
    #     if occ_cpt[id] > total_votes / 2:
    #         return id
    # return -1
    
        


if __name__ == "__main__":
    check("simple majority", winner([3, 2, 3]), 3)
    check("more votes", winner([2, 2, 1, 1, 1, 2, 2]), 2)
    check("single vote", winner([1]), 1)
    check("unanimous", winner([5, 5, 5, 5]), 5)
    check("majority is zero", winner([0, 0, 1]), 0)
    check("just over half", winner([7, 7, 7, 1, 2]), 7)
    check('negative winner', winner([-1, 2, -1]), -1)
    report()
