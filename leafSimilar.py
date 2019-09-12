from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None or root2 is None:
            return False

        def getLeaf(root):
            stack = [root]
            res = []

            while stack:
                curr = stack.pop()
                if not curr.left and not curr.right:
                    res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

            return res

        return True if getLeaf(root1) == getLeaf(root2) else False

test = Solution()
root1 = test.sortedArrayToBST([1, 2, 3, 4, 6, 9, 20])
root2 = test.sortedArrayToBST([1, 2, 3, 4, 6, 9, 10])
test1 = Solution1()
print test1.leafSimilar(root1, root2)

