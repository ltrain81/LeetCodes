class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        f = lambda m, n : True if (m+n) % 2 == 0 else False
        even = f(m, n)
        
        cnt = 1
        left = m
        right = n
        result1 = 0
        result2 = 0

        while cnt < (m+n)/2:
            if left > 0 and right > 0:
                if heapq.nsmallest(1, nums1) <= heapq.nsmallest(1, nums2):
                    heappop(nums1)
                    left -= 1
                else:
                    heappop(nums2)
                    right -= 1
            elif left > 0:
                heappop(nums1)
            elif right > 0:
                heappop(nums2)
            cnt += 1
            
        if left > 0 and right > 0:
            if heapq.nsmallest(1, nums1) <= heapq.nsmallest(1, nums2):
                result1 = heappop(nums1)
                left -= 1
            else:
                result1 = heappop(nums2)
                right -= 1
        elif left > 0:
            result1 = heappop(nums1)
            left -= 1
        elif right > 0:
            result1 = heappop(nums2)
            right -= 1
            
        if left > 0 and right > 0:
            if heapq.nsmallest(1, nums1) <= heapq.nsmallest(1, nums2):
                result2 = heappop(nums1)
                left -= 1
            else:
                result2 = heappop(nums2)
                right -= 1
        elif left > 0:
            result2 = heappop(nums1)
        elif right > 0:
            result2 = heappop(nums2)
        
        if even:
            return (result1 + result2) / 2
        else:
            return result1

        return 