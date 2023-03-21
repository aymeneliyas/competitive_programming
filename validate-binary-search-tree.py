# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self,root,low,high):
        if not root:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        left = self.isValid(root.left,low,root.val)
        right = self.isValid(root.right,root.val,high)

        return left and right
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.isValid(root,float('-inf'),float('inf'))
        return ans