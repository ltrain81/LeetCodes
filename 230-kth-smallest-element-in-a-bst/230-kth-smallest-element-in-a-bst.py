# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = []
        self.readAll(root)
        heapify(self.nums)
        
        while k > 1:
            heappop(self.nums)
            k -= 1
        
        return heappop(self.nums)
    
    def readAll(self, root):
        if root.left:
            self.readAll(root.left)
        if root.right:
            self.readAll(root.right)
        self.nums.append(root.val)
        