class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sums = []
        n = len(nums)
        
        for i in range(n-3):
            if nums[i] * 4 > target:
                break
            if i>0 and nums[i] == nums[i-1]: continue
            res = self.threeSum(nums[i+1:], target - nums[i])
            sums += [[nums[i]]+r for r in res]
        
        return sums
        
        
    def threeSum(self, nums, target):
        nums.sort()
        sums = []
        curSum = 0
        result = []
        
        if len(nums) < 3:
            return result
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            number = nums[i]
            secondIndex = i + 1
            thirdIndex = len(nums) - 1
            
            while secondIndex < thirdIndex:
                neededSum = target - (number + nums[secondIndex])
                for j in range(secondIndex, thirdIndex):
                    if neededSum == nums[thirdIndex]:
                        if [number, nums[secondIndex], nums[thirdIndex]] not in result:
                            result.append([number, nums[secondIndex], nums[thirdIndex]])
                    if neededSum > nums[thirdIndex]:
                        break
                    thirdIndex -= 1
                secondIndex += 1
                
        return result
    
        '''
        for i in range(n-3):
            first = nums[i]
            for j in range(i+1, n-2):
                second = nums[j]
                for k in range(j+1, n-1):
                    thirdIndex = k
                    third = nums[k]
                    fourthIndex = n - 1
                    need = target - (first + second + third)
                    while thirdIndex < fourthIndex:
                        if nums[fourthIndex] == need:
                            tmp = [first, second, third, nums[fourthIndex]]
                            if tmp not in sums:
                                toPrint = str(i) + str(j) + str(k) + str(fourthIndex)
                                #print(toPrint)
                                sums.append(tmp)
                        if nums[fourthIndex] < need:
                            break
                        fourthIndex -= 1
                    thirdIndex += 1
                        
        return sums        
        '''