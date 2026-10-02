class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []        
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            result.append(abs(left_sum-right_sum))
            left_sum += nums[i]
        return result