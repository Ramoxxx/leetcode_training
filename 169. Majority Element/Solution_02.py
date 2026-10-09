class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        candidate = None
        cpt = 0        
        for num in nums: 
            if num == candidate:
                cpt += 1
            else:
                if cpt == 0:
                    candidate = num
                    cpt = 1
                else:
                    cpt -= 1           

        return candidate