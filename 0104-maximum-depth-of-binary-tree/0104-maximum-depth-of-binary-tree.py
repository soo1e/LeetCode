# post order
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        max_depth = max(left_depth, right_depth) + 1
        return max_depth