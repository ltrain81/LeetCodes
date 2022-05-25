class Solution:
    def jump(self, nums: List[int]) -> int:
        #전까지 최소 횟수를 계속해서 업데이트하면 된다.
        minJump = [math.inf for i in range(len(nums))]
        minJump[0] = 0
        for i in range(len(nums)):
            jump = nums[i]
            for j in range(i+jump, i, -1):
                if j <= len(nums) - 1:
                    minJump[j] = min(minJump[j], minJump[i] + 1)
        
        #print(minJump)
        
        return minJump[len(nums) -1]
                