class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums)
        for i in range(len(nums)):
            nums[i] = -nums[i]
            
        heapify(nums)
        
        for i in range(k-1):    
            heappop(nums)
        
        return -heappop(nums)