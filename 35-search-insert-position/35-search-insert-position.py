class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cnt = 0
        n = len(nums)
        while cnt < n:
            cur = nums.pop(0)
            if cur == target:
                return cnt
            elif cur > target:
                return cnt
            else:
                cnt += 1
                
        return cnt