# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,string,root,ans):
        if not root.left and not root.right:
            ans.append(string + str(root.val))
            return 
        
        if root.right:
            self.check(string + str(root.val) +  "->" ,root.right,ans)
        if root.left:
            self.check(string + str(root.val) + "->",root.left,ans)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        st = ""
        ans = []
        self.check(st,root,ans)

        return ans