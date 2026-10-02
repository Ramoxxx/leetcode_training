class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum
        for i in range(k,len(nums)):
            current_window_sum -= nums[i-k]
            current_window_sum += nums[i]
            max_sum = max(max_sum,current_window_sum)
        return max_sum / k

