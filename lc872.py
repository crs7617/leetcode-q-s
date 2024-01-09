# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        def dfs(root):
            if root is None:
                return []

            l=dfs(root.left)+dfs(root.right)

            return l or [root.val]
        
        return dfs(root1)==dfs(root2)
