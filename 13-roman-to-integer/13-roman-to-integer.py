class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = ''
        for i, c in enumerate(s):
            if prev is 'I':
                if c is 'V' or c is 'X':
                    result -= 2
            elif prev is 'X':
                if c is 'L' or c is 'C':
                    result -= 20
            elif prev is 'C':
                if c is 'D' or c is 'M':
                    result -= 200
            n = self.determineInputChar(c)
            prev = c
            result += n
        return result
    
    def determineInputChar(self, c):
        match c:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
        