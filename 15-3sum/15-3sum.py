class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []
        curSum = 0
        result = []
        
        if len(nums) < 3:
            return result
        
        for i in range(len(nums)-2):
            number = nums[i]
            secondIndex = i + 1
            thirdIndex = len(nums) - 1
            
            while secondIndex < thirdIndex:
                neededSum = 0 - (number + nums[secondIndex])
                for j in range(secondIndex, thirdIndex):
                    if neededSum == nums[thirdIndex]:
                        if [number, nums[secondIndex], nums[thirdIndex]] not in result:
                            result.append([number, nums[secondIndex], nums[thirdIndex]])
                    if neededSum > nums[thirdIndex]:
                        break
                    thirdIndex -= 1
                secondIndex += 1
                
        return result
                    
            
            
            
            