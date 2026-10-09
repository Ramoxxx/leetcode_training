class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        seen = dict()
        maxSeen = 0
        result = 0
        for num in nums:
            seen[num] = seen.get(num,0) + 1
            if seen[num] > maxSeen:
                maxSeen = seen[num]
                result = num           

        return result
        