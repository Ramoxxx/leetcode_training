class Solution:    
    def addBinary(self, a: str, b: str) -> str:
        carry = 0        
        index1 = len(a)-1
        index2 = len(b)-1
        result = []
        while index1 >= 0 or index2 >= 0:
            
            current_sum = carry
            
            if index1 >= 0:
                digit1 = int(a[index1])
                current_sum += digit1
                       
            if(index2 >= 0):
                digit2 = int(b[index2])
                current_sum += digit2
                index2 -= 1             
            
            result.append(str(current_sum % 2))
            carry = current_sum // 2   
            
            # better perfs with this for shorts lists :
            # if current_sum == 2:
            #     result.append("0")
            #     carry = 1
            # elif current_sum == 3:
            #     result.append("1")
            #     carry = 1
            # else:
            #     result.append(str(current_sum))
            #     carry = 0            
                                         
            index1 -= 1
           
        if carry > 0:
            result.append(str(carry))       
        return "".join(reversed(result))
        
#  1111
#  1111
#  ----
# 11110
# print(Solution().addBinary("1010","1011"))
print(Solution().addBinary("1111","1111"))