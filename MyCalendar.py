# BST

class Node:
    def __init__(self,s,e):
        self.e = e
        self.s = s
        self.left = None
        self.right = None

class MyCalendar(object):
    def __init__(self):
        self.root = None
        self.res = None

    def book_helper(self, s, e, node):
        if s >= node.e:
            if not node.right:
                node.right = Node(s, e)
                self.res = True
            else:
                self.book_helper(s, e, node.right)

        elif e <= node.s:
            if not node.left:
                node.left = Node(s, e)
                self.res = True
            else:
                self.book_helper(s, e, node.left)
        else:
            self.res = False

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            self.book_helper(start, end, self.root)
            return self.res



MyCalendar = MyCalendar()
print MyCalendar.book(10, 20)
print MyCalendar.book(15, 25)
print MyCalendar.book(20, 30)

# Brutal force:
# isOverlap ==> max(start1, start2) < min(end1, end2)