class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        resS = ''
        resT = ''
        
        for i in range(len(s)):
            if s[i] == '#':
                if len(resS) > 0:
                    resS = resS[:-1]
            else:
                resS += s[i]
        
        for i in range(len(t)):
            if t[i] == '#':
                if len(resT) > 0:
                    resT = resT[:-1]
            else:
                resT += t[i]
        
        if resS == resT:
            return True
        else:
            return False
        