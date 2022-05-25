class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #condition 1: if opened, it needs to be closed 
        #condition 2: if the right order is broken, it is resetted starting from the current (if it is '(')

        max_length = 0
        stck=[-1] # initialize with a start index
        
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i) #adds index
            else:
                stck.pop()
                if not stck: # if popped -1, add a new start index
                    stck.append(i)
                else:
                    max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
        return max_length