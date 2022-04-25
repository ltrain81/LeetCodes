class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        n = len(s)
        zigzag = [[] for i in range(numRows)]
        rounds = n // (2 * numRows - 2) + 1
        
        currentRound = 1
        
        while currentRound <= rounds:
            startingIndex = (currentRound - 1) * (2 * numRows - 2)
            
            for i in range(2* numRows - 2):
                if startingIndex + i < n:
                    if i < numRows:
                        zigzag[i].append(s[startingIndex + i])
                    else:
                        rowId = 2*numRows - i - 2
                        zigzag[rowId].append(s[startingIndex + i])
                else:
                    break

            currentRound += 1
            
        result = ""
        
        print(zigzag)
        for i in range(numRows):
            result += ''.join(zigzag[i])
            
        return result
            
        