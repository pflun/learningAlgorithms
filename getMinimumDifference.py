# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return
        self.res = float('inf')
        self.all = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            self.all.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)

        for i in range(1, len(self.all)):
            if self.all[i] - self.all[i - 1] < self.res:
                self.res = self.all[i] - self.all[i - 1]

        return self.res

# Optimization O(1) space:
# prev = -float('inf')
# When traverse:
# res = min(res, curr - prev)
# prev = curr