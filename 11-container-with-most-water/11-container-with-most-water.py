class Solution:
    def maxArea(self, height: List[int]) -> int:
        XandY = []
        result = 0
        n = len(height)
        left = 0
        right = n-1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > result:
                result = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return result
        
        '''
        Solution 1:
        for x in range(n):
            XandY.append([x, height[x]])
        XandY.sort(key=lambda x: x[1], reverse = 1)
        
        for i in range(n-1):
            wall = XandY[i] #second biggest
            x = wall[0]
            for j in range(i+1,n):
                wall2 = XandY[j]
                x2 = wall2[0]
                y = wall2[1]
                #print("%d with %d, %d"%(x, x2, y))
                if result < abs(x2 - x) * y:
                    result = abs(x2 - x) * y
                
            
        return result
        '''