# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
count = 0
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        global count
        count = 0
        
        def DFS(node):
            global count
            if not node:
                return 0, 0

            left_sum, left_cnt = DFS(node.left)
            right_sum, right_cnt = DFS(node.right)

            total = node.val + left_sum + right_sum
            cnt = 1 + left_cnt + right_cnt

            if total // cnt == node.val:
                count += 1

            return total, cnt
        
        DFS(root)
        return count

    