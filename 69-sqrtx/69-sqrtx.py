class Solution:
    def mySqrt(self, x: int) -> int:
        answer = 1
        squared = 1
        while squared < x:
            answer += 1
            squared = answer * answer
        
        if squared != x:
            answer -= 1
            
        return answer