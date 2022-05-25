class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        length = 0
        
        for i in range(1, len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                length += 1
            elif nums[i] == prev:
                nums[i] = 101
        
        nums.sort()
        
        return length + 1