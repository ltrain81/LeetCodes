class Solution:
    #just like fibonacci
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        #print(nums)
        return max(nums)
        
        
        '''
        n = len(nums)
        self.maxSum = -math.inf
        self.sums = [[math.inf for i in range(n)] for j in range(n)]
        for i in range(n):
            self.calculateSum(nums, i, n-1)
        
        return self.maxSum
        
    def calculateSum(self, nums, start, end):
        #print("Now doing.. " + str(start) + " " + str(end))
        if end - start == 0:
            self.sums[start][end] = nums[start]
            #print(self.sums[start][end])
            self.maxSum = max(self.maxSum, self.sums[start][end]) 
            return nums[start]
        
        if self.sums[start][end] != math.inf:
            #print(self.sums[start][end])
            return self.sums[start][end]
        
        self.sums[start][end] = self.calculateSum(nums, start, end-1) + self.calculateSum(nums, end, end)

        self.maxSum = max(self.maxSum, self.sums[start][end])
        
        return self.sums[start][end]
        '''