class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        left = 0
        right = k
        result = None
        prev_window_tot = 0
        while right < len(nums): 
            window = (nums[left:right])           
            window_tot = 0
            if left == 0:
                window_tot = sum(window)
            else:                
                window_tot = prev_window_tot - nums[left-1] + nums[right]

            print(window)
            print(prev_window_tot)
            print(window_tot)
            
            prev_window_tot = window_tot  

            window_average = window_tot / k
            
            if not result or window_average > result:
                result = window_average

            left += 1
            right += 1

        return 0

        # not working
        # nums.sort()
        # print(nums)
        # window_sum = 0
        # for i in range(len(nums) - k,len(nums)):
        #     window_sum += nums[i]
        #     print(nums[i])
        # return window_sum / k

        # timeout
        # left = 0
        # right = k
        # result = None
        # while right <= len(nums):
        #     window = (nums[left:right])
        #     window_average = sum(window) / k
        #     if not result or window_average > result:
        #         result = window_average
        #     left += 1
        #     right += 1
        # return result