class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        index = len(digits)-1
        carry = 1
        while index >= 0:
            digit = digits[index] + carry             
            if digit == 10:
                digits[index] = 0
                carry = 1 
            else:
                digits[index] = digit 
                carry = 0               
            index -= 1 
        if carry != 0:
            digits.insert(0,carry)        
        return digits        
param = [9,8,9,9]
print(Solution().plusOne(param))