class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        Sum = 0
        result = nums[0] + nums[1] + nums[2]
            
        for i in range(n-2):
            first = nums[i]
            j, k = i+1, n - 1
            while j < k:
                Sum = first + nums[j] + nums[k]
                if target == Sum:
                    return Sum
                if abs(Sum - target) < abs(result - target):
                    result = Sum
                if Sum < target:
                    j += 1
                elif Sum > target:
                    k -= 1
        return result
        
        