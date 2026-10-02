class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        right = k
        result = None
        while right <= len(nums):
            window_average = 0
            for i in range(left,right):
                window_average += (nums[i])
            window_average = window_average / k
            if not result or window_average > result:
                result = window_average
            left += 1
            right += 1
        return result