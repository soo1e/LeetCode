# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root == None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            return root
        elif left and right:
            return root
        else:
            return left or right
        # elif left:
        #     return left
        # elif right:
        #     return right
        # else:
        #      reutrn None