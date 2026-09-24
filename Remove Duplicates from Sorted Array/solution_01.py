#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:        
        write = 1
        for read in range(1,len(nums)):
            if nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write += 1
        return write
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))