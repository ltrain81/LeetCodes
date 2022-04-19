# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.To = self.From = self.prev = None
        self.inorder(root)
        tmp1 = self.From.val
        tmp2 = self.To.val
        self.From.val = tmp2
        self.To.val = tmp1
        
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        if self.prev != None and root.val < self.prev.val:
            if(self.From == None):
                self.From = self.prev
            self.To = root
        self.prev = root
        if root.right:
            self.inorder(root.right)
            
            