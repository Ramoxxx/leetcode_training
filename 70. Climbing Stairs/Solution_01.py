class Solution:    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        #start at 3
        prev2 = 1 # number of ways for 1
        prev1 = 2 # number of ways for 2
        # current = 3 # number of ways for 3
        for _ in range(3, n+1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current 
        
        return prev1
    
# param = 8
param = 10
# param = 8
# param = 2
print("=====",Solution().climbStairs(param),sep="\n",end="\n=====")