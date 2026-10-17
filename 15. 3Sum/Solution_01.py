class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # result = set() 
        result = [] #opti (others opti make duplicate verifications useless)
        nums.sort()

        for i in range(0,len(nums)):
            if nums[i] > 0: # opti
                break
            if i > 0 and nums[i] == nums[i-1]: #opti
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1                    
                else:
                    result.append((nums[i],nums[left],nums[right]))
                    left += 1                   
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: #opti
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: #opti
                        right -= 1
        return result