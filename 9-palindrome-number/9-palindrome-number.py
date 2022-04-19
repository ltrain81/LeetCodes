class Solution:
    def isPalindrome(self, x: int) -> bool:
        Stringed = str(x)
        if Stringed[0] == '-':
            return False
        ListedInt = [int(n) for n in Stringed]
        length = len(ListedInt)
        start = 0
        end = length - 1
        if length % 2 == 0:
            half = math.ceil(length / 2)
            for i in range(half):
                if ListedInt[start] != ListedInt[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True    
        else: 
            while start <= end:
                if ListedInt[start] != ListedInt[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True
        