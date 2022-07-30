class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #case 1 : not 9
        if digits[-1] != 9:
            digits[-1] += 1
        #case 2 : 9
        else:
            digits[-1] = 0
            if len(digits) == 1:
                digits = [1] + digits
            else:
                digits = self.plusOne(digits[:-1]) + [digits[-1]]
        
        return digits
            
            