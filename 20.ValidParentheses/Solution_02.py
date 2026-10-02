class Solution:
    def isValid(self, s: str) -> bool:        
        stack = list()
        if(len(s) < 2):
            return False
        for index,char in enumerate(s):
            
            match char:
                case ")":
                    if len(stack) == 0 or index == 0 or stack.pop() != "(":
                        return False
                case "}":
                    if len(stack) == 0 or  index == 0 or stack.pop() != "{":
                        return False
                case "]":
                    if len(stack) == 0 or  index == 0 or stack.pop() != "[":
                        return False
                case _:
                    stack.append(char)

        return len(stack) == 0

        
        