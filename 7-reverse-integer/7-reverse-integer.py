class Solution:
    def reverse(self, x: int) -> int:
        Stringed = str(x)
        Minus = False
        Length = 0
        Max = '2147483647'
        zero_index = 0
        
        if x == 0:
            return x
        
        if Stringed[0] == '-':
            Stringed = Stringed[1:]
            Minus = True
        
        String_Rev = Stringed[::-1]
        Length = len(String_Rev)
        
        while zero_index < Length:
            if String_Rev[zero_index] == '0':
                zero_index += 1
            else:            
                break
                
        String_Rev = String_Rev[zero_index:]
        
        if Length < 10:
            if Minus: String_Rev = '-' + String_Rev
            return String_Rev
        elif Length > 10:
            return 0
        else:
            cnt = 0
            while cnt < 10:
                if String_Rev[cnt] < Max[cnt]:
                    if Minus: return '-' + String_Rev
                    else: return String_Rev
                elif String_Rev[cnt] > Max[cnt]:
                    return 0
                else:
                    cnt+= 1
                    
        return 0
            
        