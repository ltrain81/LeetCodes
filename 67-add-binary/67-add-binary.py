class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenDiff = len(a) - len(b)
        maxLen = 0
        result = ''
        if lenDiff > 0:
            b = '0' * lenDiff + b
            maxLen = len(a)
        else:
            a = '0' * abs(lenDiff) + a
            maxLen = len(b)
        
        a = a[::-1]
        b = b[::-1]
        prev = 0
        
        for i in range(maxLen):
            cur = int(a[i]) + int(b[i]) + prev
            if cur == 3:
                result += '1'
                prev = 1
            elif cur == 2:
                result += '0'
                prev = 1
            elif cur == 1:
                result += '1'
                prev = 0
            else:
                result += '0'
                prev = 0
        
        if prev == 1:
            result += '1'
            
        result = result[::-1]
        
        return result