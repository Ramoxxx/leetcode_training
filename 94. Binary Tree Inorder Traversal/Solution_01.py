# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        current_node = root
        result = list()
        while current_node:
            result.append(current_node.val)
            if current_node.left:
                current_node = current_node.left
            elif current_node.right:
                current_node = current_node.right
            else:
                current_node = None
        return result