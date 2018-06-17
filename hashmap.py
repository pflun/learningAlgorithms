# -*- coding:utf-8 -*-
# 一个list，每个位置存一个Node(key, val)，hash func是key变成string的长度mod list的长度

class Cell(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

class HashMap:
    def __init__(self, size):
        self.items = []
        self.count = size  # 最大表长

        for _ in range(size):
            self.items.append(None)

    def hash(self, key):
        return len(str(key)) % self.count  # 散列函数采用除留余数法

    def put(self, key, value):
        address = self.hash(key)  # 求散列地址

        if not self.items[address]:
            self.items[address] = Cell(key, value)
        else:
            curr = self.items[address]
            while curr.next:
                if curr.key == key:
                    curr.value = value
                    return
                else:
                    curr = curr.next
            # corner case last node
            if curr.key == key:
                curr.value = value
            else:
                curr.next = Cell(key, value)

    def get(self, key):
        address = self.hash(key)
        curr = self.items[address]
        if not curr:
            return None
        else:
            while curr:
                if curr.key == key:
                    return curr.value
                else:
                    curr = curr.next
            return None

test = HashMap(10)
print test.put('first', 1)
print test.put('second', 2)
print test.put('third', 3)
print test.put('theee', 4)
print test.put('theee', 5)
print test.get('theee')