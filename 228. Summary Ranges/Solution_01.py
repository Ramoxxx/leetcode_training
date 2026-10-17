class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:  
        left = 0   
        result = []   
        while left < len(nums):
            print(left)
            right = left + 1
            while right < len(nums) and nums[right] == nums[right-1] + 1:
                right += 1

            if left == right -1:
                result.append(f"{nums[left]}")
            else:
                result.append(f"{nums[left]}->{nums[right-1]}")     


               
            left = right

        return result
            
            


            


            
        