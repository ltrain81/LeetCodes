class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        self.dp = [0 for i in range(n)]
        self.dp[0] = 1
        self.dp[1] = 2
        
        for i in range(2, n):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
            
        return self.dp[n-1]
        