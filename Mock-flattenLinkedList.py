# 1 -> 2 -> 3 -> 4
#      |
#      5 -> 6
#      |
#      7
#
# 1 2 5 7 6 3 4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.down = None

class Solution(object):
    def flattenLinkedList(self, root):
        stack = [root]
        dummy = ListNode(0)

        while stack:
            curr = stack.pop()
            dummy.next = curr
            dummy = dummy.next

            if curr.next:
                stack.append(curr.next)

            if curr.down:
                stack.append(curr.down)

        # traverse = root
        # while traverse:
        #     print traverse.val
        #     traverse = traverse.next

        return root

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
seven = ListNode(7)
one.next = two
two.next = three
three.next = four
two.down = five
five.next = six
five.down = seven

test = Solution()
print test.flattenLinkedList(one)
