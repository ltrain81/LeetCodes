# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #append goals
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.goalNumbers = []
        result = self.getAllNumbers(root, k)
        
        return result
                
    
    def getAllNumbers(self, root, k):
        if root:
            if self.getAllNumbers(root.left, k):
                return True
            if self.getAllNumbers(root.right, k):
                return True
            if root.val in self.goalNumbers:
                return True
            self.goalNumbers.append(k - root.val)