class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = []
        addedIndex = []
        cnt = 0
        
        for num in nums:
            if num in needed:
                index = needed.index(num)
                return [addedIndex[index], cnt]
            needed.append(target-num)
            addedIndex.append(cnt)
            cnt += 1
            
        