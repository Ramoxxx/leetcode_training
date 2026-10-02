class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,value in enumerate(nums):
            compl = target - value
            if compl in seen:
                return [seen[compl],i]
            seen[value] = i