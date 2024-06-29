# level order
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 0
        q = deque()
        q.append((root, 1))

        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))

        return max_depth