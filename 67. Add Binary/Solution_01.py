class Solution:    
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        longest = a if len(a) > len(b) else b
        shortest = b if longest == a else a
        index1 = len(longest)-1
        index2 = len(shortest)-1
        result = []
        while index1 >= 0:
            digit1 = int(longest[index1])
            sum = digit1 + carry            
            if(index2 >= 0):
                digit2 = int(shortest[index2])
                sum += digit2
                index2 -= 1 
            
            if sum == 2:
                result.append(0,"0")
                carry = 1
            elif sum == 3:
                result.insert(0,"1")
                carry = 1
            else:
                result.insert(0,str(sum))
                carry = 0            
                                         
            index1 -= 1
           
        if carry > 0:
            result.insert(0,str(carry))       
        return "".join(result)
        
#  1111
#  1111
#  ----
# 11110
# print(Solution().addBinary("1010","1011"))
print(Solution().addBinary("1111","1111"))