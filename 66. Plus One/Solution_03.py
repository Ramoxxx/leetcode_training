class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:        
        for index in range(len(digits)-1,-1,-1):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
            index -= 1
        digits.insert(0,1)
        return digits
param = [9,2,5,9]
print(param)
print(Solution().plusOne(param))