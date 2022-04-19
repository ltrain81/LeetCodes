class Solution:
    def intToRoman(self, num: int) -> str:
        resultArray = self.determineNum(num)
        result = ''.join(resultArray)
        return result
    
    def determineNum(self, num):
        result = []
        prev = ''
        while num != 0:
            if num >= 1000:
                prev = 'M'
                mogth, num = divmod(num, 1000)
                for i in range(mogth):
                    result.append('M')
            elif num >= 500:
                prev = 'D'
                mogth, num = divmod(num, 500)
                for i in range(mogth):
                    result.append('D')
            elif num >= 100:
                mogth, num = divmod(num, 100)
                if mogth is 4:
                    if prev == 'D':
                        result.remove('D')
                        result.append('CM')
                    else:
                        result.append('CD')
                else:
                    for i in range(mogth):
                        result.append('C')
                prev = 'C'
            elif num >= 50:
                prev = 'L'
                mogth, num = divmod(num, 50)
                for i in range(mogth):
                    result.append('L')
            elif num >= 10:
                mogth, num = divmod(num, 10)
                if mogth is 4:
                    if prev == 'L':
                        result.remove('L')
                        result.append('XC')
                    else:
                        result.append('XL')
                else:
                    for i in range(mogth):
                        result.append('X')
                prev = 'X'
            elif num >= 5:
                prev = 'V'
                mogth, num = divmod(num, 5)
                for i in range(mogth):
                    result.append('V')
            else:
                mogth, num = divmod(num, 1)
                if mogth is 4:
                    if prev == 'V':
                        result.remove('V')
                        result.append('IX')
                    else:
                        result.append('IV')
                else:
                    for i in range(mogth):
                        result.append('I')
                prev = 'I'
        return result