class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(0,len(nums)):
            left_sum = 0 if i == 0 else sum(nums[0:i])
            right_sum = 0 if i == len(nums)-1 else sum(nums[i+1:len(nums)])
            # print(f"{i} -> left: {left_sum}, right: {right_sum}")
            if left_sum == right_sum:
                return i
        return -1