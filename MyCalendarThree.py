# -*- coding: utf-8 -*-
from collections import OrderedDict
# Sorted Dict, OrderedDict是alphabetical，这道题要key sort by numerical
class MyCalendarThree(object):
    def __init__(self):
        self.calendar = OrderedDict()

    def book(self, start, end):
        self.calendar[start] = self.calendar.get(start, 0) + 1
        self.calendar[end] = self.calendar.get(end, 0) - 1

        res = 0
        curr = 0

        for key, val in self.calendar.items():
            res = max(res, curr + val)

        # print self.calendar
        return res


class Node:
    def __init__(self, l, r, count):
        self.l = l
        self.m = -1
        self.r = r
        self.count = count
        self.left = None
        self.right = None

# Segment Tree
class MyCalendarThree2:
    def __init__(self):
        self.root = Node(0, 10 ** 9, 0)
        self.max = 0

    def book(self, start, end):
        self.add(start, end, self.root)
        return self.max

    def add(self, start, end, root):
        if root.m != -1:
            if end <= root.m:
                self.add(start, end, root.left)
            elif start >= root.m:
                self.add(start, end, root.right)
            else:
                self.add(start, root.m, root.left)
                self.add(root.m, end, root.right)
            return

        if start == root.l and end == root.r:
            root.count += 1
            self.max = max(self.max, root.count)
        elif start == root.l:
            root.m = end
            root.left = Node(start, root.m, root.count + 1)
            root.right = Node(root.m, root.r, root.count)
            self.max = max(self.max, root.count + 1)
        elif end == root.r:
            root.m = start;
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, root.r, root.count + 1)
            self.max = max(self.max, root.count + 1)
        else:
            root.m = start
            root.left = Node(root.l, root.m, root.count)
            root.right = Node(root.m, root.r, root.count)
            self.add(start, end, root.right)

obj = MyCalendarThree()
print obj.book(10, 20)
print obj.book(50, 60)
print obj.book(10, 40)
print obj.book(5, 15)
print obj.book(5, 10)
print obj.book(25, 55)