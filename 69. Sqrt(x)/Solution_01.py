class Solution:
    def mySqrt(self, x: int) -> int:       
        if x < 2:
            return x
        elif x == 2:
            return 1  
        for square_candidate in range(1,x):
            product = square_candidate * square_candidate            
            print(f"square : {square_candidate}, product : {product}")
            if(product == x):
                return square_candidate
            elif(product > x):
                return square_candidate-1
        return 0
param = 5625
# param = 25
param = 2
print("---",Solution().mySqrt(param),sep="\n")