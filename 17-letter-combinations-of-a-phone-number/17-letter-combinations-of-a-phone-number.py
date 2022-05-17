from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        cand = []
        result = []
        NumtoString = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m', 'n', 'o'], '7':['p','q','r','s'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        
        if n < 1: #no digits
            return []
        
        # tjrdnjs 석원 tjrdnjs 석원 rjrdnjs 석원 tjrdnjs 석원 
        for i in range(n):
            d = digits[i]
            cand.append(NumtoString[d])
             
        prod = product(*cand)
        for p in prod:
            s = ''.join(p)
            result.append(s)
        
        return result
            
            
        