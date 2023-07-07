# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        level_values = defaultdict(list)
        def dfs(node, level):
            if not node:
                return
            level_values[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        level_values = sorted(level_values.items(), key=lambda x: x[0])
        ans = []
        for level_value in level_values:
            ans.append(level_value[1])
        return ans
