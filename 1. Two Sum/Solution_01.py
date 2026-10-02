class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i,num1 in enumerate(nums):
            j = len(nums) - 1
            while j > i:
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i,j]
                # print(f"{i} -> {num1}, {j} -> {num2}")
                j -= 1