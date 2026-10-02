class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left <= right:
            middle_index = (left + right) // 2         
            current = nums[middle_index]
            
            if current == target:
                return middle_index
            if current < target:
                left = middle_index + 1
            else:
                right = middle_index - 1
            # if current < target:
            #     left = middle_index + 1
            # elif current > target:
            #     right = middle_index - 1
            # else: 
            #     return middle_index            

        return -1