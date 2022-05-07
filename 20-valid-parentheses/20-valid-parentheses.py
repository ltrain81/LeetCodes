class Solution:
    def isValid(self, s: str) -> bool:
        #queue
        openQueue = []
        
        closing = [')', '}', ']']
        opening = ['(', '{', '[']
        
        for char in s:
            if char in opening:
                openQueue.append(char)
                
            else: #closing
                if len(openQueue) == 0:
                    return False
                check = openQueue.pop()
                if char == ')' and check != '(':
                    return False
                elif char == '}' and check != '{':
                    return False
                elif char == ']' and check != '[':
                    return False
        
        if len(openQueue) == 0:
            return True
        else: return False
                    
            
            
            