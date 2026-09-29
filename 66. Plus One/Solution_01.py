class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number_str = ""
        for digit in digits:
            number_str += str(digit)
        new_number = int(number_str) + 1
        result = []
        for digit in str(new_number):
            result.append(int(digit))
        return result