class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        left_window_sum = 0
        right_window_sum = sum(nums)        
        
        for i in range(len(nums)):

            right_window_sum -= nums[i]
            if left_window_sum == right_window_sum:
                return i
            left_window_sum += nums[i]

        return -1