# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node): #[with_root,without_root]
            if not node:
                return [0,0]
            leftpair = dfs(node.left)
            rightpair = dfs(node.right)
            with_root = node.val + leftpair[1] + rightpair[1]
            without_root = max(leftpair) + max(rightpair)
            return [with_root,without_root]
        return max(dfs(root))