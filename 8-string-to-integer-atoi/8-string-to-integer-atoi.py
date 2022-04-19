class Solution:
    def myAtoi(self, s: str) -> int:
        #erase all white spaces : 1st Condition
        s = s.strip()
        resultInt = 0
        result = ""
        Input = list(s)
        sign = ""
        signed = False
        Integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        #first char to be sign? -> 2nd Condition
        if len(s) == 0:
            return 0
        
        if Input[0] in ['-', '+']:
            signed = True
            sign = Input[0]
            Input.pop(0)
            
        #3. Read in the next the chars until the next non-digit char or the end of the input is reached. The rest of the string is ignored. 
        for c in Input:
            if c not in Integers:
                break
            else:
                result += c
            
        if result != "":
            result = sign + result
            resultInt = int(result)
            if resultInt > 2**31 -1:
                return 2147483647
            elif resultInt < -(2**31):
                return -2147483648
            else:
                return resultInt
        else: return 0
        