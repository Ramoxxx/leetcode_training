# TODO : test then continue
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x // 2
        while left < right:
            print(left, right)
            if left * left == x:
                return left
            else:
                left += 1
        return right
# param = 5625
param = 25
# param = 2
print("---",Solution().mySqrt(param),sep="\n")