"""
MAXIMUM SUM OF DISTINCT SUBARRAYS WITH LENGTH K
Pattern: Sliding Window + frequency map

Given a list of integers and an integer k, look at every contiguous
window of exactly k elements. A window is "valid" only if all k
elements are distinct. Return the largest sum among all valid windows.
If no window of length k has all distinct elements, return 0.

Examples:
    max_distinct_sum([1, 5, 4, 2, 9, 9, 9], 3) -> 15
        windows of size 3: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15,
        [2,9,9] invalid, [9,9,9] invalid -> best valid = 15
    max_distinct_sum([4, 4, 4], 3) -> 0

Think about: slide a window of fixed size k across the list. Keep a
running sum and a frequency map of what is inside the window. When the
window holds k distinct values, it is a candidate. Add the entering
element, remove the leaving one, each step.
Contract:
Input values are positive integers and 1 <= k <= len(nums).
Empty lists and invalid window sizes are out of scope. Aim for O(n) time.

"""

from testkit import check, report


def max_distinct_sum(nums, k):    
    max_sum = 0
    current_sum = 0
    seen_cpt = {}
    for right in range(0, len(nums)):
       
        enter_num = nums[right]
        current_sum += enter_num
        seen_cpt[enter_num] = seen_cpt.get(enter_num,0) + 1

        if right >= k:
            exit_num = nums[right - k]
            current_sum -= exit_num
            seen_cpt[exit_num] = seen_cpt.get(exit_num,0) - 1
            if seen_cpt[exit_num] <= 0:
                seen_cpt.pop(exit_num)
            
        if right >= k-1:
          if(len(seen_cpt)) == k:
              max_sum = max(max_sum,current_sum)

           
       
    

    return max_sum
    


if __name__ == "__main__":
    check("best is a later window", max_distinct_sum([1, 5, 4, 2, 9, 9, 9], 3), 15)
    check("no valid window", max_distinct_sum([4, 4, 4], 3), 0)
    check("whole list distinct", max_distinct_sum([1, 2, 3], 3), 6)
    check("k equals one", max_distinct_sum([5, 1, 3], 1), 5)
    check("two valid windows", max_distinct_sum([1, 2, 1, 2, 3], 3), 6)
    check('becomes valid after duplicates leave', max_distinct_sum([1, 1, 2, 3], 3), 6)
    check('duplicate at window ends', max_distinct_sum([1, 2, 1], 3), 0)
    check('best window first', max_distinct_sum([9, 8, 1, 1], 2), 17)
    check('must keep exactly k', max_distinct_sum([10, 1, 2, 3], 2), 11)
    report()
